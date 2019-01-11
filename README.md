# pp-cs-tool

Archives data and stored them to onedrive

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

```bash
Python3
```

### Installing

```bash
pipenv install
```

## Running

Running requires config as an input parameter. It looks like this
```json
{
	"onedrive": {
		"id": "client_id",
		"secret": "client_secret"
	},
	"dir_path": "path_to_directory",
	"archive_pass": "password"
}
```

```bash
python main.py --config path_to_config
```

It takes a directory make an archive from it and publish it on onedrive

## Running the tests

```bash
python unittest
```


## Acknowledment
* Hat tip to anyone whose code was used

