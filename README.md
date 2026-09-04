# T-Rex Runner Clone 🦖

You know that little dinosaur game that pops up on Chrome when your internet dies? I rebuilt it from scratch in Python using Pygame, just for fun (and to get some practice with game loops, collision detection, and basic physics).

Jump over cacti, try not to die, watch the game speed up the longer you survive.

## Controls

- **Space** or **Up Arrow** — jump
- **Space** or **Up Arrow** (after you crash) — restart, no need to relaunch anything

## What's actually going on under the hood

- The dino jumps using simple gravity + velocity, nothing fancy — just enough to feel right
- Cacti spawn off-screen with random widths, heights, and gaps so it doesn't feel repetitive
- The game speeds up gradually the longer you last, so it never gets stale (or too easy)
- Basic rectangle collision detection for the "you hit a cactus, game over" moment
- Score ticks up in real time while you play

## Running it yourself

You'll need Python 3.7+ and Pygame installed.

```bash
git clone https://github.com/<your-username>/<your-repo>.git
cd <your-repo>
pip install pygame
python trex_runner.py
```

(Swap `trex_runner.py` for whatever you actually named the file.)

## Why I built this

Mostly to practice game dev fundamentals — object-oriented design for game entities, handling real-time input, gravity/physics, and managing game state (playing vs. game over vs. restart). It's a small project but it touches on a lot of the same concepts bigger games use.

## Things I might add later

- Real sprites instead of plain rectangles
- Sound effects (jump, crash)
- A high score that actually saves between runs
- Flying obstacles to mix things up
- Day/night background cycle, like the original

## License

MIT — do whatever you want with it.
