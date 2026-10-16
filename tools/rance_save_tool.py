#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Kichikuou Rance Save File Analyzer & Cheat/Creation Tool (xsystem35 / System 3.5)
Non-intrusive save data generator, editor, and cheat tool.
"""

import os
import sys
import json
import struct
import argparse
from typing import Dict, List, Optional, Tuple

COMMANDER_NAMES = {
    1: "Rance", 2: "Sill", 3: "Bound", 4: "Soul", 5: "Leila",
    6: "Barres", 7: "Rick", 8: "Cordoba", 9: "Kinkaid", 10: "Menad",
    11: "Asuka", 12: "Haurein", 13: "Melfeis", 14: "Ex", 15: "Gengorou",
    16: "Maria", 17: "Shizuka", 18: "Patton", 19: "Hanty", 20: "Freak",
    21: "Hubert", 22: "Lelyukov", 23: "Eleanor", 24: "Milli", 25: "Mill",
    26: "Đại vương Mars", 27: "Isoroku", 28: "Cream", 29: "Satella", 30: "Meglass",
    31: "Kentarou", 32: "Miki", 33: "Julia", 34: "Rafalia", 35: "Arlcoate",
    36: "Aviator", 37: "Gandhi", 38: "Chizuko", 39: "Magic", 40: "Nagi",
    41: "Galtia", 42: "Chị em Seizel", 43: "Aristoles", 44: "Gurwin", 45: "Huyền bí",
    46: "Somita", 47: "Rolex", 48: "Quân đoàn", 49: "Louis", 50: "Cecil",
    51: "Dự bị 1", 52: "Dự bị 2"
}

SLOT_FILES = {
    1: "KICHIKUSA.asd",
    2: "KICHIKUSB.asd",
    3: "KICHIKUSC.asd",
    4: "KICHIKUSD.asd",
    5: "KICHIKUSE.asd",
    6: "KICHIKUSF.asd",
    7: "KICHIKUSG.asd",
    8: "KICHIKUSH.asd",
    9: "KICHIKUSI.asd",
    10: "KICHIKUSJ.asd",
}

AVAILABLE_UNITS_BY_ARC = {
    # Arc 1: Giai đoạn Sơn tặc (Bandit Arc)
    "bandit": [1, 2, 3, 4],
    # Arc 2: Khởi nghĩa Leazas (Leazas Rebellion Arc)
    "rebellion": [1, 2, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17],
    # Arc 3: Bình định Leazas / Vua Rance (King of Leazas Arc - Arc 2 + trung lập/đánh thuê)
    "leazas": [
        1, 2, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17,
        24, 25, 26, 28, 34, 35, 36, 49, 50
    ],
    # Arc 4: Chiến dịch Helman (Helman War Arc - Arc 3 + phe Helman)
    "helman": [
        1, 2, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17,
        24, 25, 26, 28, 34, 35, 36, 49, 50,
        18, 19, 20, 21, 22, 23, 47
    ],
    # Arc 5: Chiến dịch JAPAN (Japan Arc - Arc 4 + phe JAPAN)
    "japan": [
        1, 2, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17,
        24, 25, 26, 28, 34, 35, 36, 49, 50,
        18, 19, 20, 21, 22, 23, 47,
        27, 33
    ],
    # Arc 6: Chiến dịch Zeth (Zeth War Arc - Arc 5 + phe Zeth)
    "zeth": [
        1, 2, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17,
        24, 25, 26, 28, 34, 35, 36, 49, 50,
        18, 19, 20, 21, 22, 23, 47,
        27, 33,
        37, 38, 39, 40, 43, 44, 45, 46
    ],
    # Arc 7: Chiến dịch Ma giới / Kayblis (Demon Realm War Arc - Toàn bộ tướng)
    "kayblis": [
        1, 2, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17,
        24, 25, 26, 28, 34, 35, 36, 49, 50,
        18, 19, 20, 21, 22, 23, 47,
        27, 33,
        37, 38, 39, 40, 43, 44, 45, 46,
        29, 30, 31, 32, 41, 42
    ],
}

def normalize_arc_name(name: str) -> str:
    n = name.lower().strip()
    if n in ["1", "bandit", "sontac"]:
        return "bandit"
    elif n in ["2", "rebellion", "khoinghia"]:
        return "rebellion"
    elif n in ["3", "leazas", "vua"]:
        return "leazas"
    elif n in ["4", "helman"]:
        return "helman"
    elif n in ["5", "japan"]:
        return "japan"
    elif n in ["6", "zeth"]:
        return "zeth"
    elif n in ["7", "kayblis", "magioi", "demon"]:
        return "kayblis"
    return n

def turn_to_date(turn: int) -> Tuple[int, int, int]:
    """Returns (Year LP, Month, Week) for a given turn number."""
    if turn < 1:
        turn = 1
    year = 3 + (turn - 1) // 48
    rem = (turn - 1) % 48
    month = (rem // 4) + 1
    week = (rem % 4) + 1
    return year, month, week

class RanceSaveFile:
    def __init__(self):
        self.signature: bytes = b"System3.5 SavaData(c)ALICE-SOFT\x00"
        self.version: int = 0x350200
        self.game_name: bytes = b"\x00" * 28
        self.raw_header: bytearray = bytearray(4096)
        
        self.sco_page: int = 33
        self.sco_index: int = 224
        
        self.stack_header: bytes = struct.pack('<IIII', 28, 0, 0, 0)
        # Default clean stack frame returning to MAIN.ADV (page 12)
        self.stack_data: bytes = bytes.fromhex("a1 00 00 00 01 00 00 00 01 00 00 00 ad 18 00 00 0c 00 00 00 02 00 00 00 02 00 00 00")
        
        self.str_header: bytes = struct.pack('<IIII', 0, 4999, 101, 0)
        self.str_data: bytes = b"\x00" * 12843
        
        self.pages: Dict[int, List[int]] = {
            0: [0] * 65537,
            1: [0] * 20001,
            2: [0] * 1801,
            4: [0] * 2101,
            10: [0] * 301,
        }

    @classmethod
    def load(cls, filepath: str) -> "RanceSaveFile":
        save = cls()
        with open(filepath, "rb") as f:
            data = f.read()

        if len(data) < 4096:
            raise ValueError(f"File too small to be valid .asd: {len(data)} bytes")

        save.raw_header = bytearray(data[:4096])
        save.signature = bytes(save.raw_header[:32])
        save.version = struct.unpack('<I', save.raw_header[32:36])[0]
        save.game_name = bytes(save.raw_header[36:64])
        save.sco_page, save.sco_index = struct.unpack('<ii', save.raw_header[80:88])

        stackinfo, var_str = struct.unpack('<ii', save.raw_header[2144:2152])
        var_sys = struct.unpack('<256I', save.raw_header[2160:2160+1024])

        # Stack
        st_size = struct.unpack('<I', data[stackinfo:stackinfo+4])[0]
        save.stack_header = data[stackinfo:stackinfo+16]
        save.stack_data = data[stackinfo+16:stackinfo+16+st_size]

        # Strings
        str_size = struct.unpack('<i', data[var_str:var_str+4])[0]
        save.str_header = data[var_str:var_str+16]
        save.str_data = data[var_str+16:var_str+16+str_size]

        # Variable Pages
        save.pages = {}
        for page_no, offset in enumerate(var_sys):
            if offset != 0:
                p_size = struct.unpack('<i', data[offset:offset+4])[0]
                num_elements = p_size // 2
                elements = struct.unpack(f'<{num_elements}H', data[offset+16:offset+16+p_size])
                save.pages[page_no] = list(elements)

        return save

    def save(self, filepath: str):
        # Recalculate layout
        offset = 4096
        stackinfo_offset = offset
        offset += 16 + len(self.stack_data)

        varstr_offset = offset
        offset += 16 + len(self.str_data)

        var_sys = [0] * 256
        pages_binary = []
        for p in [0, 1, 2, 4, 10]:
            if p in self.pages:
                var_sys[p] = offset
                elements = self.pages[p]
                byte_size = len(elements) * 2
                p_head = struct.pack('<iiii', byte_size, p, 0, 0)
                p_data = struct.pack(f'<{len(elements)}H', *elements)
                pages_binary.append(p_head + p_data)
                offset += len(p_head) + len(p_data)

        # Update header
        header = bytearray(self.raw_header)
        header[:32] = self.signature.ljust(32, b'\x00')
        header[32:36] = struct.pack('<I', self.version)
        header[36:64] = self.game_name.ljust(28, b'\x00')
        header[80:88] = struct.pack('<ii', self.sco_page, self.sco_index)
        header[2144:2152] = struct.pack('<ii', stackinfo_offset, varstr_offset)
        header[2160:2160+1024] = struct.pack('<256I', *var_sys)

        # Stack block
        st_head = struct.pack('<IIII', len(self.stack_data), 0, 0, 0)
        stack_block = st_head + self.stack_data

        # String block
        str_size = len(self.str_data)
        count = struct.unpack('<i', self.str_header[4:8])[0] if len(self.str_header) >= 8 else 4999
        maxlen = struct.unpack('<i', self.str_header[8:12])[0] if len(self.str_header) >= 12 else 101
        str_head = struct.pack('<iiii', str_size, count, maxlen, 0)
        str_block = str_head + self.str_data

        out_data = bytes(header) + stack_block + str_block + b"".join(pages_binary)

        # Write to file
        os.makedirs(os.path.dirname(os.path.abspath(filepath)), exist_ok=True)
        with open(filepath, "wb") as f:
            f.write(out_data)

    # --- Property Accessors ---
    @property
    def turn(self) -> int:
        return self.pages[0][517] if 0 in self.pages and len(self.pages[0]) > 517 else 1

    @turn.setter
    def turn(self, val: int):
        if 0 in self.pages and len(self.pages[0]) > 517:
            self.pages[0][517] = max(1, min(65535, val))
            # Sync date display vars
            y, m, w = turn_to_date(val)
            self.pages[0][537] = y
            self.pages[0][538] = m
            self.pages[0][539] = w

    @property
    def gold(self) -> int:
        return self.pages[0][519] if 0 in self.pages and len(self.pages[0]) > 519 else 0

    @gold.setter
    def gold(self, val: int):
        if 0 in self.pages and len(self.pages[0]) > 519:
            self.pages[0][519] = max(0, min(65535, val))

    @property
    def cp(self) -> int:
        return self.pages[0][540] if 0 in self.pages and len(self.pages[0]) > 540 else 0

    @cp.setter
    def cp(self, val: int):
        if 0 in self.pages and len(self.pages[0]) > 540:
            self.pages[0][540] = max(0, min(65535, val))

    @property
    def clear_flag(self) -> int:
        return self.pages[0][57] if 0 in self.pages and len(self.pages[0]) > 57 else 0

    @clear_flag.setter
    def clear_flag(self, val: int):
        if 0 in self.pages and len(self.pages[0]) > 57:
            self.pages[0][57] = 1 if val else 0

    @property
    def clear_count(self) -> int:
        return self.pages[4][79] if 4 in self.pages and len(self.pages[4]) > 79 else 0

    @clear_count.setter
    def clear_count(self, val: int):
        if 4 in self.pages and len(self.pages[4]) > 79:
            self.pages[4][79] = max(0, min(65535, val))

    @property
    def unlocked_cgs_count(self) -> int:
        if 4 not in self.pages or len(self.pages[4]) < 2080:
            return 0
        return sum(1 for x in self.pages[4][80:2080] if x > 0)

    def get_stage_name(self) -> str:
        p0 = self.pages.get(0, [])
        if len(p0) < 600:
            return "Không xác định"
        s = p0[518]
        if s == 0:
            return "Giai đoạn Sơn tặc Rance (Bandit Arc)"
        elif s == 1:
            if p0[59] == 1:
                return "Chiến dịch Helman (Helman War Arc)"
            elif p0[325] == 1:
                return "Chiến dịch JAPAN (Japan Arc)"
            elif p0[60] == 1:
                return "Chiến dịch Zeth (Zeth War Arc)"
            return "Giai đoạn Quân phiến loạn Leazas (Leazas Rebellion Arc)"
        elif s == 2:
            return "Giai đoạn Bình định Leazas / Vua Rance (King of Leazas)"
        elif s == 3 or p0[535] > 0:
            return "Chiến dịch Ma giới / Kayblis (Demon Realm War Arc)"
        return f"Giai đoạn {s}"

    # --- Cheat Functions ---
    def unlock_all_cgs(self):
        """Unlocks all 2000 CGs in Array 4 and all system gallery flags."""
        if 4 in self.pages:
            p4 = self.pages[4]
            for i in range(80, min(2080, len(p4))):
                p4[i] = 1
            for i in range(2080, min(2101, len(p4))):
                p4[i] = 1
        # Set system clear count to unlock album & extra menu
        self.clear_count = max(self.clear_count, 100)

    def heal_all_troops(self):
        """Sets current troops equal to max troops for all recruited commanders."""
        if 1 not in self.pages:
            return
        p1 = self.pages[1]
        for slot in range(1, 53):
            is_active = p1[19 * 52 + slot]
            if is_active:
                max_troops = p1[1 * 52 + slot]
                p1[0 * 52 + slot] = max_troops

    def boost_troops(self, amount: int = 1000):
        """Boosts max troops and current troops for all recruited commanders."""
        if 1 not in self.pages:
            return
        p1 = self.pages[1]
        for slot in range(1, 53):
            is_active = p1[19 * 52 + slot]
            if is_active:
                cur_max = p1[1 * 52 + slot]
                new_max = max(cur_max, amount)
                p1[1 * 52 + slot] = new_max
                p1[0 * 52 + slot] = new_max

    def boost_stats(self, atk: int = 15, def_: int = 15):
        """Boosts Attack and Defense for all active commanders."""
        if 1 not in self.pages:
            return
        p1 = self.pages[1]
        for slot in range(1, 53):
            is_active = p1[19 * 52 + slot]
            if is_active:
                p1[2 * 52 + slot] = max(p1[2 * 52 + slot], atk)
                p1[3 * 52 + slot] = max(p1[3 * 52 + slot], def_)

    def reset_turn_actions(self):
        """Resets all action commands so all actions are usable in current turn."""
        if 0 not in self.pages:
            return
        p0 = self.pages[0]
        for v in [542, 543, 544, 545, 546, 547, 548, 679, 680]:
            if v < len(p0):
                p0[v] = 1

    def apply_arc_preset(self, arc_name: str):
        """Applies scenario state and active commanders for a specific story arc."""
        arc = arc_name.lower()
        p0 = self.pages[0]
        p1 = self.pages[1]

        if arc in ["1", "bandit", "sontac"]:
            # Bandit Arc
            self.turn = 1
            p0[518] = 0
            p0[51] = 0
            p0[59] = 0
            p0[60] = 0
            p0[325] = 0
            p0[535] = 0
            # Active commanders: Rance (1), Sill (2), Bound (3), Soul (4)
            for slot in range(1, 53):
                p1[19 * 52 + slot] = 1 if slot in [1, 2, 3, 4] else 0

        elif arc in ["2", "rebellion", "khoinghia"]:
            # Leazas Rebellion
            self.turn = 13
            p0[518] = 1
            p0[51] = 1
            p0[59] = 0
            p0[60] = 0
            p0[325] = 0
            p0[535] = 0
            # Active commanders: Rance, Leila, Barres, Rick, Cordoba, Kinkaid, Menad, Asuka
            for slot in range(1, 53):
                p1[19 * 52 + slot] = 1 if slot in [1, 2, 5, 6, 7, 8, 9, 10, 11] else 0

        elif arc in ["3", "leazas", "vua"]:
            # King of Leazas / Liberation achieved
            self.turn = 25
            p0[518] = 2
            p0[51] = 1
            p0[58] = 1
            p0[59] = 0
            p0[60] = 0
            p0[325] = 0
            p0[535] = 0
            for slot in range(1, 53):
                p1[19 * 52 + slot] = 1 if slot in [1, 2, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17] else 0

        elif arc in ["4", "helman"]:
            # Helman War
            self.turn = 35
            p0[518] = 1
            p0[59] = 1
            p0[60] = 0
            p0[325] = 0
            for slot in range(1, 53):
                p1[19 * 52 + slot] = 1 if slot in [1, 2, 5, 6, 7, 8, 10, 16, 17, 18, 19, 20] else 0

        elif arc in ["5", "japan"]:
            # Japan Expedition
            self.turn = 45
            p0[518] = 1
            p0[325] = 1
            for slot in range(1, 53):
                p1[19 * 52 + slot] = 1 if slot in [1, 2, 5, 6, 7, 16, 17, 27] else 0

        elif arc in ["6", "zeth"]:
            # Zeth Campaign
            self.turn = 55
            p0[518] = 1
            p0[60] = 1
            for slot in range(1, 53):
                p1[19 * 52 + slot] = 1 if slot in [1, 2, 5, 7, 16, 17, 37, 38, 39, 40] else 0

        elif arc in ["7", "kayblis", "magioi", "demon"]:
            # Demon Realm War
            self.turn = 75
            p0[518] = 3
            p0[535] = 2
            for slot in range(1, 53):
                p1[19 * 52 + slot] = 1 if slot in [1, 2, 5, 7, 16, 17, 27, 29, 31, 32, 39] else 0
        else:
            raise ValueError(f"Unknown arc name: {arc_name}. Available: bandit, rebellion, leazas, helman, japan, zeth, kayblis")

        self.heal_all_troops()
        self.reset_turn_actions()

    def detect_arc(self) -> str:
        """Detects current story arc from save file variables."""
        p0 = self.pages.get(0, [])
        if len(p0) < 600:
            return "rebellion"
        s = p0[518]
        if s == 0:
            return "bandit"
        elif s == 3 or p0[535] > 0:
            return "kayblis"
        elif s == 2:
            return "leazas"
        elif s == 1:
            if p0[59] == 1:
                return "helman"
            elif p0[325] == 1:
                return "japan"
            elif p0[60] == 1:
                return "zeth"
            return "rebellion"
        return "leazas"

    def recruit_all_available_units(self, arc_name: Optional[str] = None):
        """Recruits all units that can be recruited up to the specified (or detected) arc."""
        if 1 not in self.pages:
            return
        if not arc_name:
            arc_name = self.detect_arc()
        arc_key = normalize_arc_name(arc_name)
        
        target_slots = set(AVAILABLE_UNITS_BY_ARC.get(arc_key, AVAILABLE_UNITS_BY_ARC["rebellion"]))
        
        # Also check dynamic war flags if arc_name was not explicitly forced
        p0 = self.pages.get(0, [])
        if len(p0) >= 600 and not arc_name:
            if p0[59] == 1:
                target_slots.update([18, 19, 20, 21, 22, 23, 47])
            if p0[325] == 1:
                target_slots.update([27, 33])
            if p0[60] == 1:
                target_slots.update([37, 38, 39, 40, 43, 44, 45, 46])
            if p0[535] > 0 or p0[518] == 3:
                target_slots.update([29, 30, 31, 32, 41, 42])

        p1 = self.pages[1]
        for slot in range(1, 53):
            if slot in target_slots:
                p1[19 * 52 + slot] = 1
                # If max troops is 0 (except Sill and Galtia), provide base troops
                if p1[1 * 52 + slot] == 0 and slot not in [2, 41]:
                    p1[1 * 52 + slot] = 1000
                if p1[0 * 52 + slot] == 0 and p1[1 * 52 + slot] > 0:
                    p1[0 * 52 + slot] = p1[1 * 52 + slot]
            else:
                p1[19 * 52 + slot] = 0

    def get_commanders_summary(self) -> List[Dict]:
        res = []
        if 1 not in self.pages:
            return res
        p1 = self.pages[1]
        for slot in range(1, 53):
            active = p1[19 * 52 + slot]
            cur = p1[0 * 52 + slot]
            mx = p1[1 * 52 + slot]
            atk = p1[2 * 52 + slot]
            df = p1[3 * 52 + slot]
            if active or cur > 0 or mx > 0:
                res.append({
                    "slot": slot,
                    "name": COMMANDER_NAMES.get(slot, f"Slot {slot}"),
                    "active": bool(active),
                    "troops_cur": cur,
                    "troops_max": mx,
                    "atk": atk,
                    "def": df,
                })
        return res


def inspect_save(filepath: str):
    save = RanceSaveFile.load(filepath)
    y, m, w = turn_to_date(save.turn)
    print("=" * 65)
    print(f"  THÔNG TIN FILE SAVE: {os.path.basename(filepath)}")
    print("=" * 65)
    print(f"Định dạng        : {save.signature.decode('latin1', errors='ignore').strip()}")
    print(f"Phiên bản dữ liệu: 0x{save.version:X}")
    print(f"Giai đoạn / Cốt truyện: {save.get_stage_name()}")
    print(f"Thời gian        : Lượt {save.turn} (Năm LP {y}, Tháng {m}, Tuần {w})")
    print(f"Tiền (Vàng)      : {save.gold * 100}K Vàng ({save.gold} đơn vị)")
    print(f"Lượt hành động CP: {save.cp}")
    print(f"Chế độ Clear Game: {'BẬT (Khóa mở tất cả tính năng)' if save.clear_flag else 'TẮT'}")
    print(f"Bộ sưu tập CG    : {save.unlocked_cgs_count} / 2000 CG đã mở khóa")
    print(f"Số lần Clear Game: {save.clear_count} lần")
    
    cmdrs = save.get_commanders_summary()
    active_cmdrs = [c for c in cmdrs if c["active"]]
    print("-" * 65)
    print(f"DANH SÁCH TƯỚNG ĐANG XUẤT TRẬN ({len(active_cmdrs)} tướng):")
    print(f"{'Slot':<5} {'Tên Tướng':<18} {'Quân số':<14} {'Công':<6} {'Thủ':<6}")
    print("-" * 65)
    for c in active_cmdrs:
        t_str = f"{c['troops_cur']}/{c['troops_max']}"
        print(f"{c['slot']:<5} {c['name']:<18} {t_str:<14} {c['atk']:<6} {c['def']:<6}")
    print("=" * 65)


def apply_cheat_dict(save: RanceSaveFile, config: dict):
    if "arc" in config:
        save.apply_arc_preset(config["arc"])
    if config.get("all_available_units", False) or config.get("recruit_all_available_units", False):
        arc = config.get("arc")
        save.recruit_all_available_units(arc)
    if "gold" in config:
        save.gold = int(config["gold"])
    if "cp" in config:
        save.cp = int(config["cp"])
    if "turn" in config:
        save.turn = int(config["turn"])
    if config.get("clear_flag", False):
        save.clear_flag = 1
    if config.get("unlock_all_cgs", False):
        save.unlock_all_cgs()
    if "clear_count" in config:
        save.clear_count = int(config["clear_count"])
    if config.get("heal_troops", False):
        save.heal_all_troops()
    if "boost_troops" in config:
        save.boost_troops(int(config["boost_troops"]))
    if "boost_stats" in config:
        st = config["boost_stats"]
        atk = int(st.get("atk", 15)) if isinstance(st, dict) else int(st)
        df = int(st.get("def", 15)) if isinstance(st, dict) else int(st)
        save.boost_stats(atk, df)
    if config.get("reset_actions", False):
        save.reset_turn_actions()


def find_default_template() -> str:
    candidates = ["KICHIKUSA.asd", "KICHIKUSB.asd", "KICHIKUSC.asd"]
    for c in candidates:
        if os.path.exists(c):
            return c
    raise FileNotFoundError("Không tìm thấy file mẫu .asd nào trong thư mục hiện tại.")


def interactive_menu():
    while True:
        print("\n" + "=" * 65)
        print("      CÔNG CỤ QUẢN LÝ & TẠO FILE SAVE KICHIKUOU RANCE")
        print("              (xsystem35 / Cheatmode Tool)             ")
        print("=" * 65)
        print("1. Kiểm tra / Xem thông tin file save hiện có")
        print("2. Chỉnh sửa file save hiện hữu (Max Vàng, CP, Full CG, Chiêu mộ tướng)")
        print("3. Chiêu mộ tất cả tướng khả dụng theo Arc cho file save")
        print("4. Tạo bộ Save File cho TẤT CẢ các Arc (7 Arc cốt truyện + Mở Full CG)")
        print("5. Tạo/Chỉnh sửa file save theo cấu hình cheat_config.json")
        print("6. Tạo file cấu hình cheat_config.json mẫu")
        print("0. Thoát")
        print("-" * 65)
        
        choice = input("Nhập lựa chọn của bạn (0-6): ").strip()
        
        if choice == "0":
            print("\nCảm ơn bạn đã sử dụng công cụ! Tạm biệt.")
            break

        elif choice == "1":
            print("\nCác file save hiện có:")
            found = False
            for slot, fn in SLOT_FILES.items():
                if os.path.exists(fn):
                    found = True
                    print(f"[{slot}] {fn}")
            if not found:
                print("Chưa có file save nào (.asd).")
                input("\nNhấn Enter để quay lại menu chính...")
                continue
            slot_in = input("Nhập số slot hoặc tên file cần xem (mặc định 1): ").strip()
            target = SLOT_FILES.get(int(slot_in), slot_in) if slot_in.isdigit() else (slot_in or "KICHIKUSA.asd")
            if os.path.exists(target):
                inspect_save(target)
            else:
                print(f"Không tìm thấy file: {target}")
            input("\nNhấn Enter để quay lại menu chính...")

        elif choice == "2":
            print("\nCác file save hiện có:")
            for slot, fn in SLOT_FILES.items():
                if os.path.exists(fn):
                    print(f"[{slot}] {fn}")
            slot_in = input("Nhập số slot hoặc tên file cần chỉnh sửa (mặc định 1 / KICHIKUSA.asd): ").strip()
            target = SLOT_FILES.get(int(slot_in), slot_in) if slot_in.isdigit() else (slot_in or "KICHIKUSA.asd")
            if not os.path.exists(target):
                print(f"Không tìm thấy file: {target}")
                input("\nNhấn Enter để quay lại menu chính...")
                continue
            save = RanceSaveFile.load(target)
            current_stage = save.get_stage_name()
            print(f"\nFile save đang ở: {current_stage}")
            
            recruit_in = input("Chiêu mộ tất cả tướng khả dụng tính đến Arc hiện tại? (Y/n, mặc định Y): ").strip().lower()
            if recruit_in != "n":
                save.recruit_all_available_units()
                print(" -> Đã chiêu mộ tất cả tướng khả dụng theo Arc!")
            
            save.gold = 50000  # 5,000,000 Gold
            save.cp = 20       # 20 Actions
            save.clear_flag = 1
            save.unlock_all_cgs()
            save.heal_all_troops()
            save.boost_troops(1000)
            save.boost_stats(15, 15)
            save.reset_turn_actions()
            save.save(target)
            print(f"\n[THÀNH CÔNG] Đã chỉnh sửa và lưu file: {target}!")
            inspect_save(target)
            input("\nNhấn Enter để quay lại menu chính...")

        elif choice == "3":
            print("\nCác file save hiện có:")
            for slot, fn in SLOT_FILES.items():
                if os.path.exists(fn):
                    print(f"[{slot}] {fn}")
            slot_in = input("Nhập số slot hoặc tên file cần chiêu mộ tướng (mặc định 1 / KICHIKUSA.asd): ").strip()
            target = SLOT_FILES.get(int(slot_in), slot_in) if slot_in.isdigit() else (slot_in or "KICHIKUSA.asd")
            if not os.path.exists(target):
                print(f"Không tìm thấy file: {target}")
                input("\nNhấn Enter để quay lại menu chính...")
                continue
            save = RanceSaveFile.load(target)
            current_stage = save.get_stage_name()
            print(f"\nFile save đang ở: {current_stage}")
            save.recruit_all_available_units()
            save.heal_all_troops()
            save.reset_turn_actions()
            save.save(target)
            print(f"\n[THÀNH CÔNG] Đã chiêu mộ toàn bộ tướng khả dụng của Arc vào file: {target}!")
            inspect_save(target)
            input("\nNhấn Enter để quay lại menu chính...")

        elif choice == "4":
            tmpl = find_default_template()
            print(f"\nSử dụng mẫu gốc từ: {tmpl}")
            arcs = [
                (1, "bandit", "KICHIKUSA.asd", "Slot 1 (Tự động): Arc 1 - Giai đoạn Sơn tặc"),
                (2, "rebellion", "KICHIKUSB.asd", "Slot 2: Arc 2 - Khởi nghĩa Leazas"),
                (3, "leazas", "KICHIKUSC.asd", "Slot 3: Arc 3 - Bình định Leazas / Vua Rance"),
                (4, "helman", "KICHIKUSD.asd", "Slot 4: Arc 4 - Chiến dịch Helman"),
                (5, "japan", "KICHIKUSE.asd", "Slot 5: Arc 5 - Chiến dịch JAPAN"),
                (6, "zeth", "KICHIKUSF.asd", "Slot 6: Arc 6 - Chiến dịch Zeth"),
                (7, "kayblis", "KICHIKUSG.asd", "Slot 7: Arc 7 - Chiến dịch Ma giới / Kayblis"),
            ]
            for arc_id, arc_name, out_file, desc in arcs:
                s = RanceSaveFile.load(tmpl)
                s.apply_arc_preset(arc_name)
                s.recruit_all_available_units(arc_name)
                s.unlock_all_cgs()
                s.clear_flag = 1
                s.gold = 30000
                s.cp = 15
                s.heal_all_troops()
                s.boost_troops(1000)
                s.boost_stats(14, 14)
                s.save(out_file)
                print(f" -> Đã tạo: {out_file:<15} ({desc})")
            print("\n[THÀNH CÔNG] Đã tạo xong 7 file save cho 7 Arc với Full CG & Toàn bộ tướng khả dụng!")
            input("\nNhấn Enter để quay lại menu chính...")

        elif choice == "5":
            cfg_file = "cheat_config.json"
            if not os.path.exists(cfg_file):
                print(f"Không tìm thấy file {cfg_file}. Vui lòng tạo trước bằng mục 6.")
                input("\nNhấn Enter để quay lại menu chính...")
                continue
            with open(cfg_file, "r", encoding="utf-8") as f:
                cfg = json.load(f)
            src = cfg.get("template_save", find_default_template())
            out = cfg.get("output_save", "KICHIKUSA.asd")
            s = RanceSaveFile.load(src)
            apply_cheat_dict(s, cfg)
            s.save(out)
            print(f"\n[THÀNH CÔNG] Đã tạo/chỉnh sửa file {out} từ cấu hình {cfg_file}!")
            inspect_save(out)
            input("\nNhấn Enter để quay lại menu chính...")

        elif choice == "6":
            sample_config = {
                "template_save": "KICHIKUSA.asd",
                "output_save": "KICHIKUSA.asd",
                "arc": "rebellion",
                "all_available_units": True,
                "gold": 50000,
                "cp": 20,
                "clear_flag": True,
                "unlock_all_cgs": True,
                "clear_count": 100,
                "heal_troops": True,
                "boost_troops": 1000,
                "boost_stats": {"atk": 15, "def": 15},
                "reset_actions": True
            }
            with open("cheat_config.json", "w", encoding="utf-8") as f:
                json.dump(sample_config, f, indent=4, ensure_ascii=False)
            print("\n[THÀNH CÔNG] Đã tạo file mẫu cheat_config.json!")
            input("\nNhấn Enter để quay lại menu chính...")
        else:
            print("Lựa chọn không hợp lệ, vui lòng chọn lại.")


def main():
    if sys.stdout.encoding != 'utf-8':
        try:
            sys.stdout.reconfigure(encoding='utf-8')
        except Exception:
            pass
    parser = argparse.ArgumentParser(description="Kichikuou Rance Save Tool & Cheat Mode")
    subparsers = parser.add_subparsers(dest="command", help="Lệnh cần thực hiện")

    # inspect
    p_ins = subparsers.add_parser("inspect", help="Xem thông tin chi tiết file save")
    p_ins.add_argument("file", nargs="?", default="KICHIKUSA.asd", help="Đường dẫn file .asd")

    # modify
    p_mod = subparsers.add_parser("modify", help="Chỉnh sửa / Áp dụng cheat vào file save")
    p_mod.add_argument("file", nargs="?", default="KICHIKUSA.asd", help="File save đầu vào")
    p_mod.add_argument("--out", help="File save đầu ra (mặc định ghi đè file vào)")
    p_mod.add_argument("--slot", type=int, choices=range(1, 11), help="Xuất trực tiếp vào slot (1-10)")
    p_mod.add_argument("--gold", type=int, help="Đặt số tiền (đơn vị 100K Vàng, ví dụ: 50000)")
    p_mod.add_argument("--cp", type=int, help="Đặt số lượt hành động / CP mỗi lượt")
    p_mod.add_argument("--turn", type=int, help="Đặt số lượt")
    p_mod.add_argument("--clear-flag", action="store_true", help="Bật chế độ Clear Game")
    p_mod.add_argument("--unlock-cgs", action="store_true", help="Mở khóa 100%% CG hệ thống (2000 CGs)")
    p_mod.add_argument("--clear-count", type=int, help="Đặt số lần Clear Game (ví dụ: 100)")
    p_mod.add_argument("--heal-troops", action="store_true", help="Hồi phục tối đa quân số cho tất cả tướng")
    p_mod.add_argument("--boost-troops", type=int, help="Tăng quân số tối đa cho tất cả tướng (ví dụ: 1000)")
    p_mod.add_argument("--boost-stats", type=int, help="Tăng chỉ số Công/Thủ tối thiểu (ví dụ: 15)")
    p_mod.add_argument("--reset-actions", action="store_true", help="Làm mới tất cả lệnh hành động trong lượt")
    p_mod.add_argument("--arc", choices=["bandit", "rebellion", "leazas", "helman", "japan", "zeth", "kayblis"], help="Chuyển cốt truyện sang Arc chỉ định")
    p_mod.add_argument("--all-units", action="store_true", help="Kích hoạt tất cả tướng có thể chiêu mộ tính đến Arc hiện tại")
    p_mod.add_argument("--config", help="Đọc thông số từ file JSON")

    # create-all-arcs
    p_arcs = subparsers.add_parser("create-all-arcs", help="Tạo toàn bộ save file cho 7 Arc với Full CG & Clear Game")
    p_arcs.add_argument("--template", help="File save mẫu dùng để clone")

    # gen-config
    subparsers.add_parser("gen-config", help="Tạo file cấu hình cheat_config.json mẫu")

    args = parser.parse_args()

    if not args.command:
        # If no arguments provided, launch interactive menu
        interactive_menu()
        return

    if args.command == "inspect":
        target = SLOT_FILES.get(int(args.file), args.file) if args.file.isdigit() else args.file
        inspect_save(target)
        if sys.stdin.isatty():
            try:
                input("\nNhấn Enter để kết thúc...")
            except (EOFError, KeyboardInterrupt):
                pass

    elif args.command == "modify":
        target = SLOT_FILES.get(int(args.file), args.file) if args.file.isdigit() else args.file
        save = RanceSaveFile.load(target)

        if args.config:
            with open(args.config, "r", encoding="utf-8") as f:
                cfg = json.load(f)
            apply_cheat_dict(save, cfg)

        if args.gold is not None:
            save.gold = args.gold
        if args.cp is not None:
            save.cp = args.cp
        if args.turn is not None:
            save.turn = args.turn
        if args.clear_flag:
            save.clear_flag = 1
        if args.unlock_cgs:
            save.unlock_all_cgs()
        if args.clear_count is not None:
            save.clear_count = args.clear_count
        if args.heal_troops:
            save.heal_all_troops()
        if args.boost_troops is not None:
            save.boost_troops(args.boost_troops)
        if args.boost_stats is not None:
            save.boost_stats(args.boost_stats, args.boost_stats)
        if args.reset_actions:
            save.reset_turn_actions()
        if args.arc:
            save.apply_arc_preset(args.arc)
        if args.all_units:
            save.recruit_all_available_units(args.arc)

        out_path = args.out
        if args.slot:
            out_path = SLOT_FILES[args.slot]
        if not out_path:
            out_path = target

        save.save(out_path)
        print(f"[THÀNH CÔNG] Đã lưu dữ liệu vào: {out_path}")
        inspect_save(out_path)
        if sys.stdin.isatty():
            try:
                input("\nNhấn Enter để kết thúc...")
            except (EOFError, KeyboardInterrupt):
                pass

    elif args.command == "create-all-arcs":
        tmpl = args.template or find_default_template()
        arcs = [
            (1, "bandit", "KICHIKUSA.asd", "Slot 1 (Tự động): Arc 1 - Giai đoạn Sơn tặc"),
            (2, "rebellion", "KICHIKUSB.asd", "Slot 2: Arc 2 - Khởi nghĩa Leazas"),
            (3, "leazas", "KICHIKUSC.asd", "Slot 3: Arc 3 - Bình định Leazas / Vua Rance"),
            (4, "helman", "KICHIKUSD.asd", "Slot 4: Arc 4 - Chiến dịch Helman"),
            (5, "japan", "KICHIKUSE.asd", "Slot 5: Arc 5 - Chiến dịch JAPAN"),
            (6, "zeth", "KICHIKUSF.asd", "Slot 6: Arc 6 - Chiến dịch Zeth"),
            (7, "kayblis", "KICHIKUSG.asd", "Slot 7: Arc 7 - Chiến dịch Ma giới / Kayblis"),
        ]
        for arc_id, arc_name, out_file, desc in arcs:
            s = RanceSaveFile.load(tmpl)
            s.apply_arc_preset(arc_name)
            s.unlock_all_cgs()
            s.clear_flag = 1
            s.gold = 30000
            s.cp = 15
            s.heal_all_troops()
            s.boost_troops(1000)
            s.boost_stats(14, 14)
            s.save(out_file)
            print(f" -> Đã tạo: {out_file:<15} ({desc})")
        print("\n[THÀNH CÔNG] Đã tạo xong 7 file save cho 7 Arc với Full CG & Clear Game mode!")

    elif args.command == "gen-config":
        sample_config = {
            "template_save": "KICHIKUSA.asd",
            "output_save": "KICHIKUSA.asd",
            "arc": "rebellion",
            "all_available_units": True,
            "gold": 50000,
            "cp": 20,
            "clear_flag": True,
            "unlock_all_cgs": True,
            "clear_count": 100,
            "heal_troops": True,
            "boost_troops": 1000,
            "boost_stats": {"atk": 15, "def": 15},
            "reset_actions": True
        }
        with open("cheat_config.json", "w", encoding="utf-8") as f:
            json.dump(sample_config, f, indent=4, ensure_ascii=False)
        print("[THÀNH CÔNG] Đã tạo file mẫu cheat_config.json!")

if __name__ == "__main__":
    main()
