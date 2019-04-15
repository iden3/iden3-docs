# Citrus

<img align="right" width="180px" src="https://github.com/iden3/citrus/raw/master/logo.png">

Citrus: Continuous Integration Testing running until sunrise.

Citrus is a simple continuous integration testing framework that can be
configured with scripts.

The basis of citrus is **running 5 phases for each batch**:

- Setup
- Start
- Test
- Stop
- Hooks

Each phase will execute the corresponding scripts, which can be defined
globally and per repository.

## Configuration

Each script will run through a prelude script that allows you to specify global
variables that will be available for all the scripts.

There can be any number of `setup`, `start`, `test`, `stop` and `hook` scripts.
The filename of each script must start with the name of the phase in lower
case.

The scripts for each phase will be sorted in alphabetical order; this allows
defining which scripts will run first.  This sorting is applied to the complete
set of all phase scripts (global and repository scripts together).  For
example, if a tests has two parts (send and recive) and you want to ensure that
send is run before receive, name them like this: `test_00_send` and
`test_01_recive`

All the scripts must be executable (`chmod +x script`).

All the scripts will go to the configuration folder, where the top level
contains global scripts, and each folder with a repository names contains the
scripts that will run for that repository.

The configuration folder also contains a configuration file (`config.toml`)
where you specify the list of repository urls, and further parameters like
timeouts in seconds.

See the `example` folder for a specific example.

## Options

```
Usage of ./citrus:
  -conf string
    	config directory
  -debug
    	enable debug output
  -docker
    	run tests in a docker container
  -force
    	force an initial run even if repositories were not updated
  -no-update
    	don't update the repositories
  -no-web
    	don't run the web backend
  -one-shot
    	run tests only once
  -quiet
    	output warnings and errors only
  -web-only
    	run web backend only
```

## Screenshots

![Results Screenshot](./screenshot.png)

Citrus also supports a night theme :)

## Other

The css style used in the web backend is based on the [the μ css
framework](https://bafs.github.io/mu/).

## License

GPLv3, see `LICENSE.txt`
