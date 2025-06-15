# GetAudioFromYT

A lightweight Python tool to download and convert YouTube audio streams into multiple formats.
Supports configurable codecs and bitrates via a `config.toml` file.

## 1. Install Git (optional)

Git is required if you want to clone the repository. You can install it as follows:

- **Windows**:

  1. Download and install from [https://git-scm.com/downloads](https://git-scm.com/downloads)
  2. During installation, use the default settings.

- **Debian / Ubuntu**:

  ```bash
  sudo apt update
  sudo apt install -y git
  ```

- **Arch Linux**:

  ```bash
  sudo pacman -Syu git
  ```

- **macOS (Homebrew)**:

  ```bash
  brew install git
  ````

Restart your shell and verify:

````bash
git --version
````

## 2. Project Directory Paths

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

## 3. Download or Clone the Repository

### a) With Git

```bash
git clone https://github.com/Christoph-Huebner/GetAudioFromYT.git
cd GetAudioFromYT
```

### b) Without Git

1. Download the ZIP archive from: [https://github.com/Christoph-Huebner/GetAudioFromYT](https://github.com/Christoph-Huebner/GetAudioFromYT)
2. Extract the archive.
3. In your terminal, change into the extracted directory:

```bash
cd GetAudioFromYT-main/GetAudioFromYT-main/
```

## 4. Choose Your Setup

From here you can proceed **manually** (without Docker - more difficult) or using **Docker**.

### 4A. Manual Setup (no Docker)

**1. Install Python**

- **Windows**:
  1. Download the installer from https://www.python.org/downloads/
  2. During install, enable:
     - Install pip and py.exe with administrator privileges
     - Add Python to PATH
     - Disable path length limit
  3. Open a new PowerShell and verify:
     ```powershell
     python --version
     pip install --upgrade pip
     ```

- **Debian / Ubuntu**:
  ```bash
  sudo apt update
  sudo apt install -y python3 python3-pip
  python3 --version
  pip3 install --upgrade pip
  ```

- **Arch Linux**:
  ```bash
  sudo pacman -Syu python python-pip
  python --version
  pip install --upgrade pip
  ```

- **macOS (Homebrew)**:
  ```bash
  brew install python
  python3 --version
  pip3 install --upgrade pip
  ```

**2. Install FFmpeg**

- **Windows**:
  1. Download the last stable build (not the most recent one) from https://www.gyan.dev/ffmpeg/builds/
  2. Extract (bin, doc, etc.) to `C:\Program Files (x86)\ffmpeg`
  3. Add to PATH in an elevated PowerShell:
     ```powershell
     $env = [Environment]::GetEnvironmentVariable('Path','Machine')
     [Environment]::SetEnvironmentVariable('Path', "$env;C:\Program Files (x86)\ffmpeg\bin", 'Machine')
     ```

- **Debian / Ubuntu**:
  ```bash
  sudo apt update
  sudo apt install -y ffmpeg
  ```

- **Arch Linux**:
  ```bash
  sudo pacman -Syu ffmpeg
  ```

- **macOS (Homebrew)**:
  ```bash
  brew install ffmpeg
  ```

Restart your shell and verify:
```bash
ffmpeg -version
```

**3. Install Python Packages**

In your project directory (see section 2), run with administrative privileges:

- **Debian / Ubuntu & macOS (Homebrew)**:
  ```bash
  pip3 install -r pip-packages.txt
  ```

- **Windows & Arch Linux**:
  ```bash
  pip install -r pip-packages.txt
  ```

### 4B. Docker Setup

1. **Install Docker**
   - **Windows (Docker Desktop)**
     https://docs.docker.com/desktop/setup/install/windows-install/
     - Download & install
     - Reboot
     - In Admin PowerShell, add yourself to the Docker group if needed:
       ```powershell
       Add-LocalGroupMember -Group "docker-users" -Member "<YourUser>"
       ```
   - **Debian/Ubuntu**
     https://docs.docker.com/engine/install/debian/
     ```bash
     sudo apt update
     sudo apt install -y ca-certificates curl gnupg lsb-release
     # Add Docker’s GPG key & repository, then:
     sudo apt update
     sudo apt install -y docker-ce docker-ce-cli containerd.io
     sudo usermod -aG docker $USER
     ```
   - **Arch Linux**
     ```bash
     sudo pacman -Syu docker
     sudo systemctl enable --now docker
     sudo usermod -aG docker $USER
     ```
   - **macOS (Docker Desktop)**
     https://docs.docker.com/desktop/setup/install/macos/
     - Install, then ensure Docker Desktop is running.

   After adding your user to the `docker`/`docker-users` group, **log out and log in again** or reboot.

2. **Check Docker**
   Open a new Shell and verify if docker is available:
   ```bash
   docker --version
   ```

3. **Build the Docker Image**
   In the project root:
   ```bash
   docker build -t getaudiofromyt:latest .
   ```
   _Note: The first build may take a bit longer to pull base images and install dependencies. This step is required one time, if you don't delete the docker image._

## 5. Test Run

Execute a quick test to confirm everything works. The downloaded file will appear in the `files/` folder.

- **Manual (no Docker)**

  - **Debian / Ubuntu & macOS (Homebrew)**:
    ```bash
    python3 main.py "https://www.youtube.com/watch?v=E8T17Eg2wbM" --convert --format mp3
    ```

  - **Windows & Arch Linux**:
    ```bash
    python main.py "https://www.youtube.com/watch?v=E8T17Eg2wbM" --convert --format mp3
    ```

- **Docker**
  ```bash
  docker run --rm -v "$(pwd)/files:/app/files" -v "$(pwd)/config.toml:/app/config.toml:ro" getaudiofromyt:latest "https://www.youtube.com/watch?v=E8T17Eg2wbM" --convert --format mp3
  ```

## 6. Contribution

1. Fork the repo
2. Create a branch (`git checkout -b feature/YourFeature`)
3. Commit changes (`git commit -am "Add feature"`)
4. Push (`git push origin feature/YourFeature`)
5. Open a Pull Request

## 7. License

This project is distributed under a **Non-Commercial** license. See [LICENSE](LICENSE) for details.
