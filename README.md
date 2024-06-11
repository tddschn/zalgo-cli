# zalgo-cli

A simple command line tool and [Gradio app](https://huggingface.co/spaces/tddschn/zalgo-gradio) to generate zalgo text.

- [zalgo-cli](#zalgo-cli)
  - [Demo](#demo)
    - [CLI](#cli)
    - [Gradio](#gradio)
  - [Installation](#installation)
    - [pipx](#pipx)
    - [pip](#pip)
    - [zalgo-gradio](#zalgo-gradio)
  - [Usage](#usage)
    - [CLI](#cli-1)
    - [Gradio](#gradio-1)
  - [Develop](#develop)
  - [Credits](#credits)

## Demo

### CLI

```
$ zalgo test -n 20

ṯe͕sͫť	t̿e̵s͍t̐	t̜e̼s̗tͨ	ẗe̮s̼tͥ	
t͋e̞śt̪	t̊e̎s̮t͈	ṯe͊s̗t̍	t̄e̬śt͗	
t͕e͓s͜t͕	tͯe̙s͙t͍	t̀e̊s̏t̲	t̰ẽs̕t̗	
t̘e͐s̞t̿	ẗeͣs͆t̸	t͙e͉s̑t̤	t̀e͙s̐t̋	
t͆e̟s̈́tͦ	t̛e͏s̛t͕	t̆eͮs̠tͮ	t͋e̱s͎tͦ	
```

```
# accept input from stdin, adding tons of the zalgo-thingys
# output is too crazy to be put here
$ echo 'hello world' | zalgo -n 5 -o -a1000
```

### Gradio

https://huggingface.co/spaces/tddschn/zalgo-gradio

```
$ zalgo-gradio
```

![](https://github.com/cli/cli/assets/45612704/1f55f742-fea1-4e42-9c70-321ce096f0b0)

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

### zalgo-gradio

`zalgo-gradio` requires an extra dependency to run, you can install it with `pipx install zalgo-cli[gradio]` or `pip install zalgo-cli[gradio]`.

## Usage

### CLI

You can use either `zalgo` or `zalgo-cli` to run the program.

```
$ zalgo --help

usage: zalgo [-h] [-a int] [-l int] [-n int] [-o] [-V] [str]

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
  -o, -1, --one-per-line
                        Output one Zalgo-fied string per line (default: False)
  -V, --version         show program's version number and exit

```

### Gradio

```
$ zalgo-gradio
```

Or use the hosted version at https://huggingface.co/spaces/tddschn/zalgo-gradio .

## Develop

```
$ git clone https://github.com/tddschn/zalgo-cli.git
$ cd zalgo-cli
$ poetry install
```

## Credits

Development of this project was based on https://github.com/n-1x/zalgo-cli .