# Velocity Cursor

Velocity cursor is a program that makes your mouse cursor have its velocity and bounce off the edge of the screen.

## Usage

The easiest way to use Velocity cursor is to download exe file from releases and run it.\
Additionally, you can use your own acceleration multiplier and friction values with custom arguments. When no arguments given, default acceleration is 0.5 and friction is 0.05.

```bash
velocity_cursor.exe acceleration friction
```
Both values have to be in range from 0 to 1.\
This is how they work:
> acceleration multiplier tells how fast cursor accelerates for example 0.5 = half acceleration, 1 = normal acceleration, 2 = double acceleration

> friction 1 means infinite friction and 0 means no friction

Alternatively, you can create `velocity cursor config.txt` file next to the exe and put these values as separate lines.

## Running from source code

You will need Python (tested on Python 3.11) and win32api library:

```bash
pip install pywin32
```

Rest of libraries are included with Python.

## How do I close it?!

You can either go to task manager with `ctrl + shift + esc`, find `velocity_cursor.exe` on a list and then terminate task with `delete` or button (sometimes you will need to terminate two processes)

or

open `cmd` or press `winkey + R`, then type `taskkill /f /im velocity_cursor.exe` and press `enter`

## Contributing

Pull requests are welcome, however, please take in mind that it may take a pretty long time for me to verify and accept them.

## License

[MIT](https://choosealicense.com/licenses/mit/)