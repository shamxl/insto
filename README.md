# Insto

An Instagram reporter tool

# Installation

```sh
git clone git@github.com:shamxl/insto.git
cd insto
uv sync
```

# Usage

```sh
[dev@shamxl insto]$ uv run insto --help
    ____           __      
   /  _/___  _____/ /_____ 
   / // __ \/ ___/ __/ __ \
 _/ // / / (__  ) /_/ /_/ /
/___/_/ /_/____/\__/\____/ 
                           

                                                                                                            
 Usage: insto [OPTIONS] COMMAND [ARGS]...                                                                   
                                                                                                            
╭─ Options ────────────────────────────────────────────────────────────────────────────────────────────────╮
│ --install-completion          Install completion for the current shell.                                  │
│ --show-completion             Show completion for the current shell, to copy it or customize the         │
│                               installation.                                                              │
│ --help                        Show this message and exit.                                                │
╰──────────────────────────────────────────────────────────────────────────────────────────────────────────╯
╭─ Commands ───────────────────────────────────────────────────────────────────────────────────────────────╮
│ version                                                                                                  │
│ login                                                                                                    │
╰──────────────────────────────────────────────────────────────────────────────────────────────────────────╯

```

## Example usage

```sh
[dev@shamxl insto]$ uv run insto login <YOUR_SESSION_ID>
```

# TODO

- [x] fix login issue
- [ ] add who unfollowed you list
- [ ] add profile tracking