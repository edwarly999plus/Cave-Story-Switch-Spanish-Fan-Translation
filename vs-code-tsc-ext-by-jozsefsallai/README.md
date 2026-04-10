# TSC for Visual Studio Code

This extension for Visual Studio code will provide syntax highlighting, auto-completion, and diagnostics for the TSC scripting format used in the game Cave Story and other related games.

The extension implements the [TSC Language Server](https://github.com/nimblebun/tsc-language-server) and the [.tscrc.json spec](https://docs.nimblebun.works/tscrc-json)

## Features

- Syntax highlighting

<img width="1184" height="535" alt="image" src="https://github.com/user-attachments/assets/b0f58baf-fb57-4235-ab4e-bd6e86cc7834" />

- Command autocompletion

<img width="1496" height="716" alt="image" src="https://github.com/user-attachments/assets/6262e29b-3cb2-4250-9c8b-64b31560f9be" />

<img width="691" height="407" alt="image" src="https://github.com/user-attachments/assets/65bfd06c-1194-4e57-b1ad-79fdeca03d1b" />


- Command syntax checker

<img width="1055" height="414" alt="image" src="https://github.com/user-attachments/assets/1bc157ec-ef76-4eda-85e5-151cdf869ea1" />

- Helpful messages for commands on hover

<img width="1147" height="331" alt="image" src="https://github.com/user-attachments/assets/1f8fca63-9d1b-4e33-bcab-e7d2c3815744" />

- Event duplication checker

<img width="1027" height="465" alt="image" src="https://github.com/user-attachments/assets/bbf35745-aff7-4ed6-9b82-d2f101dc1fa7" />

- Warning on messagebox overflow

<img width="1404" height="361" alt="image" src="https://github.com/user-attachments/assets/d0d0a37e-0bef-4b7b-bd98-762570c235e7" />

## Contribution

**1. Clone the repo:**

```sh
git clone git@github.com:jozsefsallai/tsc-language-tooling.git
```

**2. Install the dependencies:**

```sh
npm i
```

**3. Watch or compile:**

```sh
npm run watch
npm run compile
```

Don't forget to make sure that your changes pass the linter:

```sh
npm run lint
```

## License

MIT. Cave Story (Doukutsu Monogatari) is the property of Daisuke "Pixel" Amaya and Nicalis, Inc.
