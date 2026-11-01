"""Build Pronoun Studio into a single standalone windowless executable."""
from pathlib import Path
import os
import shutil
import subprocess
import sys
import zipfile

APP = Path(__file__).resolve().parent

def make_icon():
    from PIL import Image, ImageDraw, ImageFont
    sizes = [256, 128, 64, 48, 32, 16]
    images = []
    for s in sizes:
        im = Image.new('RGBA', (s, s), (0, 0, 0, 0))
        draw = ImageDraw.Draw(im)
        rad = max(2, int(s * 0.22))
        pad = max(1, int(s * 0.04))
        draw.rounded_rectangle([pad, pad, s - pad - 1, s - pad - 1], radius=rad, fill='#c5e6aa', outline='#163d35', width=max(1, int(s * 0.04)))
        try:
            font = ImageFont.truetype('arialbd.ttf', int(s * 0.58))
        except Exception:
            try:
                font = ImageFont.truetype('segoeui.ttf', int(s * 0.58))
            except Exception:
                font = ImageFont.load_default()
        bbox = draw.textbbox((0, 0), 'P.', font=font)
        w = bbox[2] - bbox[0]
        h = bbox[3] - bbox[1]
        x = (s - w) // 2 - bbox[0]
        y = (s - h) // 2 - bbox[1]
        draw.text((x, y), 'P.', font=font, fill='#173e35')
        images.append(im)
    ico_path = APP / 'app.ico'
    images[0].save(ico_path, format='ICO', sizes=[(s, s) for s in sizes], append_images=images[1:])
    return ico_path

def main():
    print("Building PronounStudio.exe (single windowless executable)...")
    ico_path = make_icon()

    dist_build = APP / 'dist_build'
    work_dir = APP / 'build'
    dist_dir = APP / 'dist'
    dist_dir.mkdir(exist_ok=True)

    web_data = f"{APP / 'web'}{os.pathsep}web"
    cmd = [
        sys.executable, '-m', 'PyInstaller',
        '--noconfirm',
        '--clean',
        '--onefile',
        '--windowed',
        '--name', 'PronounStudio',
        '--icon', str(ico_path),
        '--add-data', web_data,
        '--collect-all', 'PIL',
        '--distpath', str(dist_build),
        '--workpath', str(work_dir),
        '--specpath', str(work_dir),
        str(APP / 'app.py')
    ]
    trust_file=Path(sys.base_prefix)/'Lib/codex-rejected-cas.pem'
    if trust_file.exists():cmd[3:3]=['--add-data',f'{trust_file}{os.pathsep}.']

    print("Running PyInstaller:", " ".join(cmd))
    res = subprocess.run(cmd, cwd=str(APP))
    if res.returncode != 0:
        raise SystemExit(f"PyInstaller failed with code {res.returncode}")

    built_exe = dist_build / 'PronounStudio.exe'
    if not built_exe.is_file():
        raise SystemExit(f"Build output not found at {built_exe}")

    # Close any running instances before overwriting
    try:
        subprocess.run(['taskkill', '/F', '/IM', 'PronounStudio.exe'], capture_output=True)
    except Exception:
        pass
    import time
    time.sleep(0.5)

    # Copy to pronoun_editor/PronounStudio.exe
    target_local = APP / 'PronounStudio.exe'
    shutil.copy2(built_exe, target_local)
    print(f"Copied executable to {target_local} ({target_local.stat().st_size:,} bytes)")

    # Copy to dist/PronounStudio.exe
    target_dist = dist_dir / 'PronounStudio.exe'
    shutil.copy2(built_exe, target_dist)
    print(f"Copied executable to {target_dist} ({target_dist.stat().st_size:,} bytes)")

    # Package zip in dist/
    zip_path = dist_dir / 'PronounStudio-Windows.zip'
    with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as z:
        z.write(built_exe, 'PronounStudio/PronounStudio.exe')
        z.write(APP / 'README.md', 'PronounStudio/README.md')
        if (APP / 'examples').is_dir():
            for f in (APP / 'examples').rglob('*'):
                if f.is_file():
                    z.write(f, Path('PronounStudio') / f.relative_to(APP))
    print(f"Packaged distribution zip: {zip_path} ({zip_path.stat().st_size:,} bytes)")

    # Clean up temp build folder
    try:
        shutil.rmtree(dist_build, ignore_errors=True)
        shutil.rmtree(work_dir, ignore_errors=True)
    except Exception:
        pass

    print("Build complete!")

if __name__ == '__main__':
    main()
