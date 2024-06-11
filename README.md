# zalgo-cli

A simple command line tool to generate zalgo text.

- [zalgo-cli](#zalgo-cli)
  - [Demo](#demo)
  - [Installation](#installation)
    - [pipx](#pipx)
    - [pip](#pip)
  - [Usage](#usage)
  - [Develop](#develop)

## Demo

```
$ zalgo test -n 20

ṯe͕sͫť	t̿e̵s͍t̐	t̜e̼s̗tͨ	ẗe̮s̼tͥ	
t͋e̞śt̪	t̊e̎s̮t͈	ṯe͊s̗t̍	t̄e̬śt͗	
t͕e͓s͜t͕	tͯe̙s͙t͍	t̀e̊s̏t̲	t̰ẽs̕t̗	
t̘e͐s̞t̿	ẗeͣs͆t̸	t͙e͉s̑t̤	t̀e͙s̐t̋	
t͆e̟s̈́tͦ	t̛e͏s̛t͕	t̆eͮs̠tͮ	t͋e̱s͎tͦ	
```

## Installation

### pipx

This is the recommended installation method.

```
$ pipx install zalgo-cli
```

### [pip](https://pypi.org/project/zalgo-cli/)

```
$ pip install zalgo-cli
```

## Usage

You can use either `zalgo` or `zalgo-cli` to run the program.

```
$ zalgo --help

usage: zalgo [-h] [-a int] [-l int] [-n int] [-o] [str]

Generate Zalgo text

positional arguments:
  str                   Initial string to Zalgo-fy. If not provided, read from
                        stdin (default: None)

options:
  -h, --help            show this help message and exit
  -a int, --adds-per-char int
                        Number of additions per character (default: 1)
  -l int, --char-limit int
                        Character limit [0 for no limit] (default: 0)
  -n int, --amount int  Amount of Zalgo text to generate (default: 1)
  -o, --one-per-line    Output one Zalgo-fied string per line (default: False)
```

## Develop

```
$ git clone https://github.com/tddschn/zalgo-cli.git
$ cd zalgo-cli
$ poetry install
```