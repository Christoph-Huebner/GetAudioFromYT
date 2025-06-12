## Installation Guide

Follow these instructions to set up GetAudioFromYT on Windows, Linux, or macOS.

### Prerequisites

- **PowerShell (Windows)**
  - `PS-Admin>`: Start PowerShell as Administrator
  - `PS>`: Start PowerShell as Standard User
- **Terminal (Linux & macOS)**: Use your default shell (bash, zsh, etc.)

### 1. Install Git (optional)

Download and install from:

[https://git-scm.com/downloads](https://git-scm.com/downloads)

Use the default settings during installation.

---

### 2. Project Directory Paths

Use one of the following working directory paths depending on how you obtained the project:

**a) With Git**

- **Windows (PowerShell):**
  ```powershell
  C:\Users\<YourUser>\Downloads\GetAudioFromYT
  ```
- **Linux (bash/zsh):**
  ```bash
  /home/<youruser>/Downloads/GetAudioFromYT
  ```
- **macOS (Terminal):**
  ```bash
  /Users/<youruser>/Downloads/GetAudioFromYT
  ```

**b) Without Git (ZIP download)**

After downloading and extracting the ZIP archive, note the `-main` suffix in the folder names:

- **Windows (PowerShell):**
  ```powershell
  C:\Users\<YourUser>\Downloads\GetAudioFromYT-main\GetAudioFromYT-main
  ```
- **Linux (bash/zsh):**
  ```bash
  /home/<youruser>/Downloads/GetAudioFromYT-main/GetAudioFromYT-main
  ```
- **macOS (Terminal):**
  ```bash
  /Users/<youruser>/Downloads/GetAudioFromYT-main/GetAudioFromYT-main
  ```

### 3. Download or Clone the Repository

#### a) With Git

```powershell
PS> git clone https://github.com/Christoph-Huebner/GetAudioFromYT.git
PS> cd GetAudioFromYT
```

#### b) Without Git

1. Download the ZIP archive from: [https://github.com/Christoph-Huebner/GetAudioFromYT](https://github.com/Christoph-Huebner/GetAudioFromYT)
2. Extract the archive.
3. In your terminal, change into the extracted directory:

```bash
cd GetAudioFromYT-main/GetAudioFromYT-main/
```

---

### 4. Install Python

Download and install from:

[https://www.python.org/downloads/](https://www.python.org/downloads/)

Enable the following options during installation:

- **Install pip and py.exe** with administrative privileges
- **Add Python to PATH**
- **Disable path length limit**

After installation, open a new shell as administrator and verify:

```powershell
PS-Admin> python --version
PS-Admin> pip install --upgrade pip
```

---

### 5. Install FFmpeg

#### Windows

1. Download a stable build (not the most recent one) from: [https://www.gyan.dev/ffmpeg/builds/](https://www.gyan.dev/ffmpeg/builds/)
2. Extract the archive.
3. Copy the extracted `ffmpeg` folder to: `C:\\Program Files (x86)\\ffmpeg`
4. In an Administrator shell, add FFmpeg to the system PATH:

```powershell
PS-Admin> $envVar = [Environment]::GetEnvironmentVariable('Path', 'Machine')
PS-Admin> $newPath = "$envVar;C:\\Program Files (x86)\\ffmpeg\\bin"
PS-Admin> [Environment]::SetEnvironmentVariable('Path', $newPath, 'Machine')
```

#### Debian / Ubuntu

```bash
sudo apt update
sudo apt install ffmpeg
```

#### Arch Linux

```bash
sudo pacman -Syu ffmpeg
```

#### macOS

```bash
brew install ffmpeg
```

5. Restart your shell and verify:

```bash
ffmpeg -version
```

---

### 6. Install Python Packages

In your project directory (see section 2), run:

```powershell
PS-Admin> pip install -r pip-packages.txt
```

---

### 7. Test Run

Execute a quick test to confirm everything works:

```bash
python main.py --url "https://www.youtube.com/watch?v=E8T17Eg2wbM" --convert --format mp3
```

The downloaded file will appear in the `files/` folder.
