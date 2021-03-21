# README

## Description

A working template to use [antlr 4](https://www.antlr.org) generated parsers with python 3.  
This sample is fitted to PL/SQL language.  
Could be used to parse any other language by providing your own .g4 Lexer & Grammar definitions.  

## Licence

Grammar definition was taken from [antlr/grammars-v4](https://github.com/antlr/grammars-v4/tree/master/sql/plsql)  

The software in this repo is also under [Apache licence, Version 2.0](http://www.apache.org/licenses/LICENSE-2.0)  
Copyright (c) 2021 Basilio Carrero Nevado

## Prerequisites

+ [java](https://www.java.com/es/download/)
+ Python modules:

    ```bash
    pip install antlr4-python3-runtime
    ```

## Usage

1. Clone this repo

    ```bash
    git clone https://bitbucket.org/Basiliocn/pyplsqlparser/src/master/
    ```

2. Build the antlr4 parser:

    ```bash
    java -jar antlr-4.9.2-complete.jar -Dlanguage=Python3 -visitor pyPlSqlLexer.g4
    java -jar antlr-4.9.2-complete.jar -Dlanguage=Python3 -visitor pyPlSqlParser.g4
    ```

3. Run It!:

    ```bash
    python funCallFinder.py ./examples-sql-script/anonymous_block.sql
    ```
