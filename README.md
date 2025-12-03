# RoboChallenge

RoboChallenge is a collection of robotics challenges, primarily used for schools outreach and currently built around the LEGO MINDSTORMS EV3 platform. Each challenge is designed to introduce students to core robotics concepts, give them a taste of being a roboticist with an enticing hands‑on activity, and, most importantly, to have fun while learning.

## Available sessions

Each challenge revolves around a workshop sheet which guides students through the activity, with accompanying starter code and other resources.

Current sessions include:

- [**RoboRacers**](https://github.com/bennett-j/RoboChallenge/tree/session-RoboRacers)
  A fast-paced introduction to robotics. Write programs to get the robot to move and use a sensor to let the robot see and follow a line.

- [**RoboRacers‑Algorithms**](https://github.com/bennett-j/RoboChallenge/tree/session-RoboRacers-Algorithms)
  This one is designed to make you think! First we get to grips with writing programs that make robots move around. We then understand how a sensor allows the robot to see the world. Finally we design algorithms that tell the robot how to use the sensor information to race along a line.

Each session has its own branch in this repository containing the materials for that particular workshop, while this branch contains the shared development code and tooling.

If you are here to lead a session, start with our [leader's notes](docs/leader_notes.md).

## Development

### Repository structure

The repository is organised as follows:

- `shared/` – common resources reused across sessions:
  - `shared/programs/` – shared EV3 Python programs
  - `shared/worksheet/` – shared LaTeX sources, styles, and images for worksheets
  - `shared/track/` – materials for the racetrack
- `sessions/` – session‑specific materials:
  - each directory defines a session (for example `RoboRacers`, `RoboRacers-Algorithms`);
  - `session.yaml` summarises the session (name, description, duration, suitability, objectives, authors) and lists the code files to include in a release;
  - `worksheet/main.tex` is the entry point for the session worksheet.
- `docs/` – supporting documentation, including [leader's notes](docs/leader_notes.md)
- `scripts/` – helper scripts used by the release workflow
- `.vscode/` – recommended editor configuration for LaTeX and EV3 development
- `.github/workflows/release.yaml` – GitHub Actions workflow to build and publish session releases
- `README.md`, `LICENSE`, and other top‑level files

### Development workflows

- **Shared resources**: keep common code and worksheet assets in `shared/` wherever possible, and only diverge in `sessions/<SessionName>/` when something is specific to that session.  
- **Session configuration**: keep each session’s `session.yaml` in sync with the actual files used in that session so releases include the correct programmes.
- **Worksheets**:
  1. Install a LaTeX distribution (for example TeX Live or MiKTeX) so that `pdflatex` is on your `PATH`.
  2. Open this repository in VS Code and install the recommended extensions when prompted.
  3. Edit the appropriate `worksheet/main.tex` file for the session.
  4. Use LaTeX Workshop’s **Build LaTeX project** command (or rely on auto‑build on save) and review the generated `main.pdf`.
- **Robot programmes**:
  1. Follow the [leader's notes](docs/leader_notes.md) for installing EV3DEV and connecting to the robot.
  2. Edit or add Python files in `shared/programs/` or `sessions/<SessionName>/programs/` as appropriate.
  3. Ensure any new or renamed files are listed in the relevant `session.yaml`.

### Building worksheets (PDFs)

In CI, the GitHub Actions workflow installs LaTeX and runs `pdflatex` to produce `main.pdf` for the session being released, including the correct version and licence information. Locally, the recommended setup is Visual Studio Code with the [LaTeX Workshop](https://marketplace.visualstudio.com/items?itemName=James-Yu.latex-workshop) extension:

- `.vscode/extensions.json` recommends `james-yu.latex-workshop` for LaTeX editing and building.
- `.vscode/settings.json` configures LaTeX Workshop to:
  - use `pdflatex` as the build tool,
  - build automatically on file changes,
  - clean up auxiliary files after a successful build,
  - open the generated PDF in a VS Code tab.


### Releasing changes

Releases are created per session using a GitHub Actions workflow defined in `.github/workflows/release.yaml`. A release packages:

- the built worksheet PDF for the chosen session,
- the Python programs and other files listed in that session’s `session.yaml`,
- a session‑specific `README.md` generated from `session.yaml`,

Trigger the workflow by pushing a tag of the form `SessionName/vX.Y` (for example `RoboRacers/v2.0` or `RoboRacers-Algorithms/v2.0`), where the session name before the `/` matches a directory under `sessions/`. Tags whose version contains `test` (for example `RoboRacers/v2.0-test`) create a draft release and a `session-SessionName-test` deployment branch, which is useful for trial runs.

On each run the workflow will:

1. Build the worksheet PDF for the selected session.
2. Copy the files listed in `session.yaml` plus `.vscode` and `LICENSE` into a clean temporary directory.
3. Generate a session‑specific `README.md` describing the session, version, duration, suitability, and objectives.
4. Create an orphan deployment branch (for example `session-RoboRacers`) containing just the release artefacts.
5. Create or update a GitHub Release for the tag, attaching the worksheet PDF (`SessionName.pdf`) and a zip archive of the Python programmes.

A typical release flow for a new RoboRacers‑Algorithms version is:

```bash
git checkout RoboRacers-Algorithms        # or your preferred development branch
# … make and commit your changes …
git tag RoboRacers-Algorithms/v2.0
git push origin RoboRacers-Algorithms/v2.0
```

GitHub Actions will then build and publish the release for you.

## RoboChallenge Contributors

Thanks to the authors who have contributed to this work and those who have supported it, including University of East Anglia science outreach.

- [James Bennett](https://github.com/bennett-j)
- [Harry Rogers](https://github.com/Harry-Rogers)
- [Charlotte Harris](https://github.com/charkharris)

## Licence

[RoboChallenge](https://github.com/bennett-j/RoboChallenge) © 2025 by James Bennett and RoboChallenge Contributors is licensed under [CC BY-SA 4.0](https://creativecommons.org/licenses/by/4.0/).