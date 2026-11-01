"""Portable, dependency-free dialogue adapters and explicit pronoun edits."""
from pathlib import Path
import copy
import hashlib
import json
import re
import textwrap

PRONOUNS = ['Đức Thánh Cha', 'Sự Thánh Thiện của cậu', 'các bạn', 'các anh',
 'chúng tôi', 'chúng ta', 'bọn ta', 'bọn tôi', 'các ngươi', 'anh ta', 'cô ta',
 'ông ta', 'anh ấy', 'cô ấy', 'bệ hạ', 'ngài', 'ta', 'tôi', 'tao', 'tớ', 'mình',
 'ngươi', 'mày', 'bạn', 'anh', 'chị', 'em', 'cô', 'ông', 'bà', 'hắn', 'nàng',
 'chàng', 'nó', 'con', 'cha', 'mẹ', 'chú', 'bác', 'cậu',
 'công tử', 'tiểu thư', 'huynh trưởng', 'đại ca', 'sơ', 'đầu lĩnh', 'lão đại',
 'thảo dân', 'thuộc hạ', 'thiện tín', 'công chúa', 'tướng quân', 'đại nhân',
 'thống lĩnh', 'tiểu đệ', 'bần đạo', 'gã này', 'bản tọa', 'quân sư', 'chúa công']
SELF = {'tôi', 'ta', 'tao', 'tớ', 'chúng tôi', 'chúng ta', 'bọn ta', 'bọn tôi',
        'thảo dân', 'thuộc hạ', 'tiểu đệ', 'bần đạo', 'gã này', 'bản tọa'}
CALL = {'ngươi', 'mày', 'các ngươi', 'các bạn', 'bệ hạ', 'đức thánh cha',
        'công tử', 'tiểu thư', 'huynh trưởng', 'đại ca', 'sơ', 'đầu lĩnh',
        'lão đại', 'đại nhân', 'tướng quân', 'công chúa', 'thống lĩnh', 'chúa công'}
LITERAL = re.compile(r"^(\s*)'(.*)'(R?)(\s*)$")

CHARACTER_NAMES = {
    'ゼイド': 'Zade', 'アトル': 'Athol', 'シルティン': 'Cyltan', 'ホエルン': 'Hoelun',
    'トロイ': 'Troy', 'ボナセル': 'Bonacel', 'プロディ': 'Prody', 'デューン': 'Dune',
    'ジャン': 'Jean', 'アッシュ': 'Ash', 'ハルディア': 'Haldyn', 'メルディ': 'Merida',
    'チェザル': 'Cezar', 'ザイード': 'Zayid', 'シーラ': 'Sheela', 'シーゼル': 'Theodel',
    'エイル': 'Yaeri', 'ルビナ': 'Rubina', 'リリア': 'Lilia', 'アコルト': 'Accorte',
    'アイネリア': 'Aynellia', 'エルヴァ': 'Urven', 'リティア': 'Lyttia', 'タリス': 'Tallan',
    'ヘルム': 'Helme', 'マーヤ': "Ma'aya", 'ネイラ': 'Neira', 'ジャムラン': 'Jamulan',
    'リンカ': 'Lianka', 'ヒルダ': 'Hilda', 'ジークフリート': 'Siegfried', 'スライン': 'Slayne',
    'エダル': 'Eddard', 'アスラン': 'Aslanne', 'ゾイ': 'Zoy', 'アリシャ': 'Alysia',
    'ラヴィニア': 'Ravinia', 'ジスカール': 'Gyskhal', 'カリエラ': 'Calliera', 'ヴェニス': 'Vanice',
    'ネイリ': 'Neere', 'ニーナ': 'Nina', 'ゼクス': 'Zech', 'アシュラム': 'Ashram',
    'スジャー packaging': 'Sujata', 'オルフェリア': 'Orphelia', 'マスード': 'Masood', 'ガーラン': 'Garlan',
    'ゴメス': 'Gormes', 'バレリウス': 'Valerius', 'マタグロス': 'Matagroth', 'マレーネ': 'Marlena',
    'ボーンワース': 'Beorn', 'ディアボリスト': 'Diabolist', 'タムティール': 'Tamthir', 'フラッペ': 'Flabbe',
    'コグロー': 'Koguro', 'エノス': "E'noth", 'ズニフ': 'Zurne', 'ベトン': 'Stigton',
    'ドーソン': 'Dawes', 'バール': 'Barl', 'オルサン': 'Olsan', 'シーベン': 'Sinnes',
    'ダリアン': 'Dundal', 'ヨーマン': "Yo'mun", 'ツワイラス': 'Zweiras', 'ベイモンク': 'Baymonk',
    'クリストバル': 'Christobal', 'ジャスロウ': 'Mummar', 'ドロンゴ': 'Boggar', 'サラエボ': 'Sarajevo',
    'ドゥルキン': 'Dulcan', 'エルシド': 'Elsid', 'ゴーウェン': 'Goewen', 'ハラシュ': 'Jarath',
    'リジン': 'Riejin', 'ギムマン': 'Gansuk', 'ルグラン': 'Legrand', 'テレニアス': 'Therenius',
    'ライアン': 'Rionet', 'オニール': 'Onfroi', 'キーラ': 'Kiera', 'イルマン': 'Inigo',
    'クロムウェル': 'Cromwell', 'シン': 'Jinn', 'アデレード': 'Adelaide', 'ダッハウェ': 'Dalgren',
    'グロムイコ': 'Maguire', 'ヘッケンバウアー': 'Hagedorn', 'ハモンド': 'Hammond', 'ケビン': 'Colm',
    'スグルト': 'Seward', 'パール': 'Pallo', 'クリスティーナ': 'Christiane', 'ハルマーン': 'Halmund',
    'マラガス': 'Marragas', 'サジャ': 'Saja', 'エルサ': 'Elsa'
}

PORTRAIT_NAMES = {
    0: 'None',
    1: 'Rance',
    2: 'Sill',
    3: 'Bound',
    4: 'Soul',
    5: 'Lia',
    6: 'Maris',
    7: 'Leila',
    8: 'Menad',
    9: 'Kanami',
    10: 'Haurein',
    11: 'Melfeis',
    12: 'Unga',
    13: 'Rebecca',
    14: 'Cell',
    15: 'Anacelle',
    16: 'Mercy',
    17: 'Ruberan',
    18: 'Sheela',
    19: 'Stessel',
    20: 'Stessel',
    21: 'Shariella',
    22: 'Shariella',
    23: 'Shariella',
    24: 'Isoroku Yamamoto',
    25: 'Kouhime',
    26: 'Cream',
    27: 'Aoi',
    28: 'Katyusha',
    29: 'Saulnia',
    30: 'Saulnia',
    31: 'Camilla',
    32: 'Mokomoko',
    33: 'Makoto',
    34: 'Horaga',
    35: 'Kayblis',
    36: 'Wendy',
    37: 'Suzume',
    38: 'Elizabeth',
    39: 'Amiran',
    40: 'Amiran',
    41: 'Amiran',
    42: 'Gandhi',
    43: 'Chizuko',
    44: 'Papaya',
    45: 'Nagi',
    46: 'Somita',
    47: 'Somita',
    48: 'Somita',
    49: 'Shizuka',
    50: 'Maria',
    51: 'Sill',
    52: 'Annis',
    53: 'Annis',
    54: 'Miki',
    55: 'Kentarou',
    56: 'Red Eye',
    57: 'Red Eye',
    58: 'Magic',
    59: 'Sieg',
    60: 'Sieg',
    61: 'Chizuko',
    62: 'Kapara',
    63: 'Merim',
    64: 'Sanakia',
    65: 'Reili',
    66: 'Ran / Eleanor',
    67: 'Milli',
    68: 'Mill',
    69: 'Mill',
    70: 'Mill',
    71: 'Suke-san',
    72: 'Kaoru',
    73: 'Silky',
    74: 'Warg',
    75: 'Satella',
    76: 'Aviator',
    77: 'Arlcoate',
    78: 'Rafalia',
    79: 'Aya',
    80: 'Cafe',
    81: 'Julia',
    82: 'Pie-R',
    83: 'Martina',
    84: 'PG-7',
    85: 'PG-9',
    86: 'Martina',
    87: 'Martina',
    88: 'Kỵ sĩ Carfe',
    89: 'Cecil',
    90: 'Louis',
    91: 'Martina',
    92: 'Martina',
    93: 'Martina',
    94: 'Saitou',
    95: 'Saitou',
    96: 'Color',
    97: 'Cordoba',
    98: 'Tougen',
    99: 'Elena',
    100: 'Fuuka',
    246: 'Kayb-one',
    247: 'Kayb-nyan',
    248: 'Chaos',
    249: 'Hồn ma',
    250: 'Bóng đen',
    252: 'Bóng đen',
    253: 'Athena 2',
    254: 'Lính canh Zeth',
    255: 'Hoàng tử quái vật',
    256: 'Tường thành',
    257: 'Xacalite',
    258: 'Melfeis',
    259: 'Melfeis',
    260: 'Menad',
    261: 'Kinkaid',
    262: 'Barres',
    263: 'Sanakia',
    352: 'Alice',
    356: 'Alice',
    357: 'Alice',
    365: 'Saitou',
    366: 'Alice',
    368: 'Alice',
    380: 'Lập trình viên WAO',
    381: 'WAO',
    382: 'Suzu',
    383: 'WAO',
    384: 'Hầu gái AliceSoft',
    385: 'AliceSoft Staff',
    386: 'AliceSoft Staff',
    387: 'AliceSoft Staff',
    388: 'AliceSoft Staff',
    390: 'Orion',
    395: 'AliceSoft Staff',
    397: 'AliceSoft Staff',
    401: 'Ruberan',
    402: 'Barres',
    403: 'Rick',
    404: 'Cordoba',
    405: 'Ex',
    406: 'Kinkaid',
    407: 'Pegasus',
    408: 'Shangri-La',
    409: 'Shangri-La',
    410: 'Nữ quan Leazas',
    411: 'Thị trưởng Ice / Reili',
    412: 'Hào kiệt Diphtheria',
    413: 'Gengorou',
    414: 'Đại vương Mars',
    415: 'Kayblis',
    416: 'Kesselring',
    417: 'Nobunaga Oda',
    418: 'Noberu Maeda',
    419: 'Washi Tada',
    420: 'Katsuie',
    421: 'Ninja JAPAN',
    422: 'Sát thủ JAPAN',
    423: 'Patton',
    424: 'Hanty',
    425: 'Hubert',
    426: 'Freak',
    427: 'Mineva',
    428: 'Saizel',
    429: 'Saizel',
    430: 'Asuka',
    431: 'Dodge',
    432: 'Aristoles',
    433: 'Convert',
    434: 'Lelyukov',
    435: 'Tami',
    436: 'Maha',
    437: 'Nero',
    438: 'Pamela',
    439: 'Alexei',
    440: 'Ortega',
    441: 'Freak / Omega',
    442: 'Camilla',
    443: 'Graco (Rockearth)',
    444: 'Satella',
    445: 'Lei',
    446: 'Lei',
    447: 'Meglass',
    448: 'Cordoba',
    449: 'Freia / Ninja',
    450: 'Medusa',
    451: 'Kaito',
    452: 'Galtia',
    453: 'Red Eye',
    454: 'Babora',
    455: 'Medusa / Sứ đồ Alefgard',
    456: 'Saias',
    457: 'Uspira',
    458: 'Kabachahn',
    459: 'Magic',
    460: 'Rebecca',
    461: 'La Vaswald',
    462: 'Olhound',
    463: 'Thánh kỵ sĩ',
    464: 'Giáo hoàng AL',
    465: 'Giáo sĩ AL',
    466: 'Camilla',
    467: 'Carol',
    468: 'Nagi / Ragarl',
    469: 'Hầu gái Kesselring',
    470: 'Thương nhân',
    471: 'Nữ quan / Hầu cận',
    472: 'Soul',
    473: 'Binh sĩ',
    474: 'Sakanaku',
    475: 'Jibul',
    476: 'Horaga',
    477: 'Takeege',
    478: 'Rue / Thuộc hạ Chizuko',
    479: 'Binh sĩ Leazas',
    480: 'Ninja Suzume',
    481: 'Britti',
    482: 'Kayb-nyan',
    483: 'Strength / Silky',
    484: 'Côn đồ / Bound',
    485: 'Ngụy thiên thần',
    486: 'Giáo sĩ AL',
    487: 'Seconaot',
    488: 'Contaot',
    489: 'Salbenaot',
    490: 'King Dragon (KD)',
    491: 'Đại diện Giáo hoàng',
    492: 'Alefgard',
    493: 'Pastel Kalar',
    494: 'Somita',
    495: 'Vua Hanny',
    496: 'Giám mục AL',
    497: 'Giám định viên',
    498: 'Rolex',
    499: 'Hoàng tử quái vật'
}

def digest(data):
    return hashlib.sha256(data).hexdigest()

def tokens(text, extra=()):
    terms = sorted(set(PRONOUNS) | {x for x in extra if x}, key=len, reverse=True)
    pattern = r'(?<!\w)(?:' + '|'.join(re.escape(s) for s in terms) + r')(?!\w)'
    return [dict(start=m.start(), end=m.end(), text=m[0],
                 role='self' if m[0].casefold() in SELF else
                      'call' if m[0].casefold() in CALL else 'unknown')
            for m in re.finditer(pattern, text, re.I)]

def replace_roles(text, spans, replacements):
    """Only selected occurrences are replaced; never a whole-script substitution."""
    previous = -1
    for s in sorted(spans, key=lambda x: x['start']):
        a, b = s['start'], s['end']
        if not isinstance(a, int) or not isinstance(b, int) or a < previous or not 0 <= a < b <= len(text):
            raise ValueError('Invalid or overlapping pronoun selection. Reload the dialogue.')
        if text[a:b] != s['text']:
            raise ValueError('Pronoun positions are stale. Reload the dialogue.')
        previous = b
    result = text
    for s in sorted(spans, key=lambda x: x['start'], reverse=True):
        new = replacements.get(s['role'])
        if new:
            old = text[s['start']:s['end']]
            if old[:1].isupper():
                new = new[:1].upper() + new[1:]
            result = result[:s['start']] + new + result[s['end']:]
    return result

def parse_adv(raw, encoding='utf-8'):
    text = raw.decode(encoding)
    lines = text.splitlines(keepends=True)
    helpers = {m[1]: int(m[2]) for m in re.finditer(
        r'^\*(L_[0-9a-f]+):\s*\n\s*!VAR0*521 : (\d+)!', text, re.M)}
    rows, scene, portraits, slot, value, width, font = [], 'entry', {}, None, None, 28, 24
    i = 0
    while i < len(lines):
        line = lines[i].rstrip('\r\n')
        if line.startswith('*'):
            scene = line[1:].rstrip(':')
            # Branch entry cannot inherit a proven speaker from linear order.
            portraits, slot, value = {}, None, None
        m = re.search(r'!VAR0*516 : (\d+)!', line)
        if m:
            value = int(m[1])
        elif re.search(r'!VAR0*516 :', line):
            value = None
        c = re.fullmatch(r'\s*\\(L_[0-9a-f]+):', line)
        op = helpers.get(c[1]) if c else None
        if op in (311, 321, 331): portraits[op // 10 % 10] = value
        elif op in (312, 322, 332): portraits.pop(op // 10 % 10, None)
        elif op in (111, 112, 121, 122): slot, width, font = op // 10 % 10, 28, 24
        elif op in (113, 123): slot, width, font = None, 28, 24
        elif op == 131: slot, width, font = None, 50, 24
        f = re.fullmatch(r'\s*ZM (\d+):', line)
        if f: font = int(f[1])
        match = LITERAL.fullmatch(line)
        if not match:
            i += 1
            continue
        indices, pieces = [i], [match[2]]
        inline = bool(match[3])
        j = i + 1
        while j < len(lines):
            k = j + 1 if lines[j].strip() == 'R' else j if inline else -1
            nxt = LITERAL.fullmatch(lines[k].rstrip('\r\n')) if 0 <= k < len(lines) else None
            if not nxt: break
            indices.append(k); pieces.append(nxt[2]); inline = bool(nxt[3]); j = k + 1
        dialogue = ' '.join(pieces)
        named = re.match(r'^([^「\n]{1,48})「', dialogue)
        hint = portraits.get(slot)
        spk_name = PORTRAIT_NAMES.get(hint, '') if hint is not None else ''
        rows.append(dict(id=f'{scene}:{i+1}', text=dialogue, original=dialogue,
                         lines=[n+1 for n in indices], indices=indices, scene=scene,
                         speaker=named[1].strip() if named else '', addressee='',
                         speaker_hint=hint, speaker_name=spk_name,
                         width=width, font=font, spans=tokens(dialogue)))
        i = j
    return rows

def parse_srpg_json(data, extra=()):
    scene_default = data.get('mapName') or data.get('name') if isinstance(data, dict) else ''
    rows = []

    def walk(obj, path, current_scene=''):
        scene = current_scene
        if isinstance(obj, dict):
            if obj.get('name') and isinstance(obj['name'], str):
                scene = obj['name']
            if obj.get('type') == 'message' and isinstance(obj.get('data'), list):
                raw_spk = obj.get('speaker', '')
                spk = CHARACTER_NAMES.get(raw_spk, raw_spk)
                for i, text in enumerate(obj['data']):
                    if isinstance(text, str):
                        p = path + ['data', i]
                        rows.append(dict(
                            id='.'.join(map(str, p)),
                            path=p,
                            original=text,
                            text=text,
                            speaker=spk,
                            raw_speaker=raw_spk,
                            addressee='',
                            scene=scene or scene_default or 'Dialogue',
                            lines=[],
                            spans=tokens(text, extra)
                        ))
            elif obj.get('type') == 'choice' and isinstance(obj.get('data'), list):
                for i, text in enumerate(obj['data']):
                    if isinstance(text, str):
                        p = path + ['data', i]
                        rows.append(dict(
                            id='.'.join(map(str, p)),
                            path=p,
                            original=text,
                            text=text,
                            speaker='Lựa chọn',
                            raw_speaker='',
                            addressee='',
                            scene=scene or scene_default or 'Choice',
                            lines=[],
                            spans=tokens(text, extra)
                        ))
            for k, v in obj.items():
                walk(v, path + [k], scene)
        elif isinstance(obj, list):
            for i, v in enumerate(obj):
                walk(v, path + [i], scene)

    walk(data, [], scene_default)
    return rows

def parse_json(raw, encoding='utf-8', extra=()):
    data = json.loads(raw.decode(encoding))
    if isinstance(data, list) and (not data or (isinstance(data[0], dict) and 'text' in data[0])):
        items = data
    elif isinstance(data, dict) and isinstance(data.get('dialogues'), list):
        items = data['dialogues']
    else:
        return parse_srpg_json(data, extra=extra)

    rows = []
    for i, item in enumerate(items):
        if not isinstance(item, dict) or not isinstance(item.get('text'), str):
            raise ValueError(f'JSON dialogue {i} needs a string text field.')
        rows.append(dict(id=str(i), original=item['text'], text=item['text'],
                         speaker=str(item.get('speaker', '')), addressee=str(item.get('addressee', '')),
                         scene=str(item.get('scene', '')), lines=[], spans=tokens(item['text'], extra)))
    return rows

def render_adv(raw, rows, encoding='utf-8',font_path=None):
    lines=raw.decode(encoding).splitlines(keepends=True);patches=[];fonts={};ImageFont=None
    if font_path is not None and Path(font_path).exists():
        try:from PIL import ImageFont
        except ImportError:pass
    for row in rows:
        if row['text']==row['original']:continue
        if any(c in row['text'] for c in "'\\\r\n\x00"):
            raise ValueError(f"{row['id']}: ADV dialogue cannot contain apostrophes, backslashes or newlines.")
        limit=min(row['width'],(600 if row['width']==50 else 336)//max(1,row['font']//2))
        font=None
        if ImageFont is not None:
            if row['font'] not in fonts:fonts[row['font']]=ImageFont.truetype(str(font_path),row['font'])
            font=fonts[row['font']]
        pixel_limit=600 if row['width']==50 else 336
        wrapped=[];line=''
        for word in row['text'].split():
            if len(word)>limit or (font and font.getlength(word)>pixel_limit):
                raise ValueError(f"{row['id']}: a word exceeds the dialogue width.")
            candidate=(line+' '+word).strip()
            if line and (len(candidate)>limit or (font and font.getlength(candidate)>pixel_limit)):
                wrapped.append(line);line=word
            else:line=candidate
        if line:wrapped.append(line)
        capacity=max(3,len(row['indices']))
        if len(wrapped)>capacity or any(len(line)>limit for line in wrapped):
            raise ValueError(f"{row['id']}: text exceeds its {capacity}-line dialogue box at {limit} characters per line. Shorten it before compiling.")
        start,end=row['indices'][0],row['indices'][-1]+1
        match=LITERAL.fullmatch(lines[start].rstrip('\r\n'));tail=LITERAL.fullmatch(lines[end-1].rstrip('\r\n'))
        indent=match[1];ending=lines[start][len(lines[start].rstrip('\r\n')):] or '\n';replacement=[]
        for i,prose in enumerate(wrapped or ['']):
            replacement.append(indent+"'"+prose+"'"+(tail[3] if i==len(wrapped)-1 else '')+ending)
            if i<len(wrapped)-1:replacement.append(indent+'R'+ending)
        patches.append((start,end,replacement))
    for start,end,replacement in sorted(patches,reverse=True):lines[start:end]=replacement
    output=''.join(lines).encode(encoding)
    if command_skeleton(raw.decode(encoding))!=command_skeleton(output.decode(encoding)):
        raise ValueError('Gameplay command preservation check failed.')
    return output

def command_skeleton(text):
    # Literal text and R line breaks are layout. Every other command, including
    # all window/wait calls and labels, must stay byte-for-byte in order.
    return '\n'.join(line for line in text.splitlines() if line.strip()!='R' and not LITERAL.fullmatch(line))


def roundtrip_literals(text):
    # xsys35dc emits extra escapes before double quotes inside ADV literals.
    # This is the same normalization used by this project's review validators.
    text = re.sub(r'\\+(?=")', '', text)
    return re.findall(r"^\s*'(.*)'R?\s*$|^\s*MS\s+\d+,\s*\"(.*)\":", text, re.M)

def render_json(raw, rows, encoding='utf-8'):
    data = json.loads(raw.decode(encoding))
    if rows and 'path' in rows[0]:
        for row in rows:
            if row['text'] == row['original']:
                continue
            path = row['path']
            target = data
            for p in path[:-1]:
                target = target[p]
            target[path[-1]] = row['text']
        return (json.dumps(data, ensure_ascii=False, indent=2) + '\n').encode(encoding)

    items = data if isinstance(data, list) else data['dialogues']
    for row in rows:
        item = items[int(row['id'])]
        item.update(text=row['text'], speaker=row['speaker'], addressee=row['addressee'])
    return (json.dumps(data, ensure_ascii=False, indent=2) + '\n').encode(encoding)

def guide_rules(text):
    """Read explicit machine blocks, AliceSoft style cells, and Vestaria Saga Markdown tables."""
    rules, warnings = [], []
    for m in re.finditer(r'```pronouns\s*\n(.*?)```', text, re.S):
        try:
            block = json.loads(m[1])
            for rule in block:
                if not all(isinstance(rule.get(k), str) and rule[k].strip()
                           for k in ('speaker', 'addressee', 'self', 'call')):
                    raise ValueError('Each rule needs speaker, addressee, self and call strings.')
                rules.append({**rule, 'source': 'Markdown pronouns block', 'line': text[:m.start()].count('\n')+1})
        except (ValueError, TypeError, AttributeError) as e:
            warnings.append(str(e))
    for lineno, line in enumerate(text.splitlines(), 1):
        if not line.startswith('|') or ':---' in line: continue

        matched_cell = False
        for cell in line.split('|'):
            m = re.search(r'\*\*([^*]+)\*\*\s+xưng\s+`([^`]+)`,\s*gọi\s+([^`]+?)\s+`([^`]+)`\s*$', cell)
            n = re.search(r'\*\*([^*]+)\*\*\s+gọi\s+([^:]+):\s*`([^`]+)`\s*\(xưng\s*`([^`]+)`\)\s*$', cell)
            if m: speaker, own, target, call = m.groups()
            elif n: speaker, target, call, own = n.groups()
            else: continue
            matched_cell = True
            rules.append(dict(speaker=speaker.strip(), addressee=target.strip(), self=own, call=call,
                              source=line, line=lineno, context='Default; inspect the source row for exceptions.'))
        if matched_cell: continue

        cells = [c.strip() for c in line.strip('|').split('|')]
        if len(cells) < 2: continue

        if any(h in cells[0] for h in ['Người nói', 'Nhân vật', 'Phân tầng', 'Đối tượng', 'Thuật ngữ']):
            continue

        col0 = re.sub(r'[*_`]', '', cells[0]).strip()
        col1 = re.sub(r'[*_`]', '', cells[1]).strip() if len(cells) > 1 else ''

        if '⬌' in col0 and len(cells) >= 3:
            pair = [p.strip() for p in col0.split('⬌')]
            p_terms = re.findall(r'`([^`]+)`', cells[2])
            context = cells[3] if len(cells) > 3 else ''
            s0 = p_terms[0] if p_terms else cells[2]
            s1 = p_terms[1] if len(p_terms) > 1 else ''
            rules.append(dict(speaker=pair[0], addressee=pair[1], self=s0, call=s1,
                              context=context, line=lineno, source=line))
            if len(pair) > 1:
                rules.append(dict(speaker=pair[1], addressee=pair[0], self=s1, call=s0,
                                  context=context, line=lineno, source=line))
            continue

        if len(cells) >= 4 and col0 and col1:
            p_self = re.findall(r'`([^`]+)`', cells[2])
            p_call = re.findall(r'`([^`]+)`', cells[3])
            context = cells[4] if len(cells) > 4 else ''
            if p_self or p_call:
                rules.append(dict(
                    speaker=col0,
                    addressee=col1,
                    self=' / '.join(p_self) if p_self else cells[2],
                    call=' / '.join(p_call) if p_call else cells[3],
                    context=context,
                    line=lineno,
                    source=line
                ))
    return rules, warnings

def match_rules(rules, speaker, addressee):
    def norm(name):
        return re.sub(r'[\(（].*?[\)）]', '', name).strip().casefold()
    s_clean = norm(speaker)
    a_clean = norm(addressee)
    return [r for r in rules if norm(r['speaker']) == s_clean and norm(r['addressee']) == a_clean]
