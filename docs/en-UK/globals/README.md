# Globals

## Table of Contents
1. [Aliases](/docs/en-UK/globals/aliases/README.md)
2. [Log](#log)

## Log

A logger. That's it. View the [diagrams](#logger-implementation)

### Logger Implementation:

```mermaid
classDiagram
    class LoggingLevel {
        <<enumeration>>
        DEBUG
        INFO
        WARNING
        ERROR
        CRITICAL
    }
    class Logger {
        +Optional~String~ name
        +Optional~String~ format
        +Optional~LoggingLevel~ level
        #set_level(LoggingLevel level) null
        +add_console() null
        +add_file(String file) null
        +full_setup(String filename) null
        +console_only() null
        +file_only(String filename) null
        +log(String message, LoggingLevel level) null
    }
    Logger o-- LoggingLevel
```