# zalgo-cli

A simple command line tool and [Gradio app](https://huggingface.co/spaces/tddschn/zalgo-gradio) to generate zalgo texts, or de-zalgo texts.

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
    - [Library](#library)
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

**Specifying a list of unicode codepoints to zalgo-fy the text**

See https://www.compart.com/en/unicode/block/U+0300

```
# add `t' diacratic marks (U+036D) on t 100 times, then add `c' diacratic marks on c 100 times
$ zalgo 'tc' -a100 -c '0x036D 0x0368'
tͭͭͭcͨͨͨ	
```

**De-zalgo-fy the text**

```
$ zalgo -z 'Z̐ȃļg̡ò'
Zalgo
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

usage: zalgo [-h] [-a int] [-l int] [-n int] [-o] [-c str] [-d] [-z] [-V]
             [str]

Generate or De-Zalgo text

positional arguments:
  str                   Initial string to Zalgo-fy or De-Zalgo-fy. If not
                        provided, read from stdin (default: None)

options:
  -h, --help            show this help message and exit
  -a int, --adds-per-char int
                        Number of additions per character (default: 1)
  -l int, --char-limit int
                        Character limit [0 for no limit] (default: 0)
  -n int, --amount int  Amount of Zalgo text to generate (default: 1)
  -o, -1, --one-per-line
                        Output one Zalgo-fied string per line (default: False)
  -c str, --codepoints str
                        Codepoints to Add (space-separated hex values, e.g.,
                        '0x036D 0x0368') (default: )
  -d, --debug           Enable debug logging (default: False)
  -z, --dezalgo         De-Zalgo-fy the input string (default: False)
  -V, --version         show program's version number and exit


```

### Gradio

```
$ zalgo-gradio
```

Or use the hosted version at https://huggingface.co/spaces/tddschn/zalgo-gradio .

### Library

Codes are split into separate files so that you can use it as a library too without hassle.

There's only one core function that you might want to use:

```python
from zalgo_cli import zalgo
```

Read the source code to see how to use it.

## Develop

```
$ git clone https://github.com/tddschn/zalgo-cli.git
$ cd zalgo-cli
$ poetry install
```

## Credits

Initial development of this project was inspired by https://github.com/n-1x/zalgo-cli .