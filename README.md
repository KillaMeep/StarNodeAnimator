<p align="center">
    <h1 align="center">StarNodeAnimator</h1>
</p>
<p align="center">
    <em>Breathtaking Star Connections, No GUI Required.</em>
</p>

<br><!-- TABLE OF CONTENTS -->
<details open>
  <summary>Table of Contents</summary><br>

- [ Overview](#overview)
- [ Features](#features)
- [ Repository Structure](#repository-structure)
- [ Modules](#modules)
- [ Getting Started](#getting-started)
  - [ Installation](#installation)
  - [ Usage](#usage)
- [ Contributing](#contributing)
</details>
<hr>

##  Overview

StarNodeAnimator is an open-source software project that uses OpenGL through Pygame to generate visually engaging star animations. Its core functionalities include creating random stars with adjustable size and node generation chances, rendering them into frames, merging the frames into an MP4 video, and offering both GUI and command-line interfaces for users convenience. By providing features like user-defined screen dimensions, colors, and a Star class for generating and connecting star nodes, this project offers an immersive and versatile solution for creating captivating star animation videos.

---

##  Features

|    |   Feature         | Description |
|----|-------------------|---------------------------------------------------------------|
| 📄 | **Documentation** | Each module has a brief description, while functions and classes are documented. The README file contains instructions for installation, and usage
| ⚡️  | **Performance**   | Optimized through efficient OpenGL rendering, Pygame handling, and resource management, creating animations efficiently with minimal resource usage. |
| 📦 | **Dependencies**  | The project depends on Python (3.7+) and Pygame library for GUI and OpenGL rendering. |

---

##  Repository Structure

```sh
└── StarNodeAnimator/
    ├── LICENSE
    ├── README.md
    ├── cooker-gui-v1.py
    ├── cooker-opengl.py
    └── main.py
```

---

##  Modules

<details open><summary>.</summary>

| File                                                                                               | Summary                                                                                                                                                                                                                                                                                                                                                                                           |
| ---                                                                                                | ---                                                                                                                                                                                                                                                                                                                                                                                               |
| [cooker-opengl.py](https://github.com/KillaMeep/StarNodeAnimator.git/blob/master/cooker-opengl.py) | Create visually stunning star animations by running this script, cooker-opengl.py. It sets up an OpenGL environment using Pygame, generates random stars with variable sizes and nodes creation chances, renders stars, captures frames, saves them as PNGs, merges them into an MP4 video, and cleans up the frames directory. This is purely visual.                                              |
| [cooker-gui-v1.py](https://github.com/KillaMeep/StarNodeAnimator.git/blob/master/cooker-gui-v1.py) | Pygame initiates a graphical user interface, initializing screen dimensions and defining colors. Stars are created with random coordinates, sizes, speeds, and a chance to generate nodes. Connections form between qualifying star pairs. Animation frames are captured, saved, and compiled into an MP4 video..                                                                                  |
| [main.py](https://github.com/KillaMeep/StarNodeAnimator.git/blob/master/main.py)                   | Initiates an animation project, setting up Pygame environment with defined screen dimensions, colors, and a Star class for creating stars. Randomly generates 200 stars, moves them within the screen boundaries, and draws circles on the screen. Stars that meet a certain criterion create lines connecting them. The loop continually redraws the screen based on user events and frame rate. This is purely visual. This is a good example of the non-opengl animation loop. |

</details>

---

##  Getting Started

**System Requirements:**

* **Python**: `version x.y.z`

###  Installation

<h4>From <code>source</code></h4>

> 1. Clone the StarNodeAnimator repository:
>
> ```console
> $ git clone https://github.com/KillaMeep/StarNodeAnimator.git
> ```
>
> 2. Change to the project directory:
> ```console
> $ cd StarNodeAnimator
> ```
>
> 3. Install the dependencies:
> ```console
> $ pip install -r requirements.txt
> ```

###  Usage

<h4>From <code>source</code></h4>

> Run StarNodeAnimator using the command below:
> ```console
> $ python coooker-gui-v1.py
> ```

---

##  Contributing

Contributions are welcome! Here are several ways you can contribute:

- **[Report Issues](https://github.com/KillaMeep/StarNodeAnimator.git/issues)**: Submit bugs found or log feature requests for the `StarNodeAnimator` project.
- **[Submit Pull Requests](https://github.com/KillaMeep/StarNodeAnimator.git/blob/main/CONTRIBUTING.md)**: Review open PRs, and submit your own PRs.
- **[Join the Discussions](https://github.com/KillaMeep/StarNodeAnimator.git/discussions)**: Share your insights, provide feedback, or ask questions.

<details closed>
<summary>Contributing Guidelines</summary>

1. **Fork the Repository**: Start by forking the project repository to your github account.
2. **Clone Locally**: Clone the forked repository to your local machine using a git client.
   ```sh
   git clone https://github.com/KillaMeep/StarNodeAnimator.git
   ```
3. **Create a New Branch**: Always work on a new branch, giving it a descriptive name.
   ```sh
   git checkout -b new-feature-x
   ```
4. **Make Your Changes**: Develop and test your changes locally.
5. **Commit Your Changes**: Commit with a clear message describing your updates.
   ```sh
   git commit -m 'Implemented new feature x.'
   ```
6. **Push to github**: Push the changes to your forked repository.
   ```sh
   git push origin new-feature-x
   ```
7. **Submit a Pull Request**: Create a PR against the original project repository. Clearly describe the changes and their motivations.
8. **Review**: Once your PR is reviewed and approved, it will be merged into the main branch. Congratulations on your contribution!
</details>

<details closed>
<summary>Contributor Graph</summary>
<br>
<p align="center">
   <a href="https://github.com{/KillaMeep/StarNodeAnimator.git/}graphs/contributors">
      <img src="https://contrib.rocks/image?repo=KillaMeep/StarNodeAnimator.git">
   </a>
</p>
</details>

---
