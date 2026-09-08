# Odoo Employee Asset Request

An Odoo 19 addon developed as part of an Associate Software Engineer take-home assignment.

## Module

**Employee Asset Request** (`employee_asset_request`)

The module allows employees to submit requests for company assets and provides a simple workflow for submitting, approving, rejecting, and resetting requests.

## Features

* Employee asset request management
* Employee selection
* Asset type selection
* Request reason
* Request date
* Request status tracking
* Submit requests
* Approve requests
* Reject requests
* Reset requests to draft
* List and form views
* Basic access rights

## Supported Assets

* Laptop
* Monitor
* Phone
* Keyboard
* Mouse
* Other

## Workflow

```text
Draft → Submitted → Approved
                  ↘ Rejected
```

Requests can also be returned to **Draft** using **Reset to Draft**.

## Requirements

* Odoo 19.0
* PostgreSQL
* Python
* Odoo `hr` module

## Installation

Copy the `employee_asset_request` directory into an Odoo addons directory, add the directory to `addons_path`, restart Odoo, update the Apps List, and install **Employee Asset Request**.

## Module Structure

```text
odoo-task/
└── employee_asset_request/
    ├── models/
    ├── security/
    ├── views/
    ├── __init__.py
    ├── __manifest__.py
    └── README.md
```

## Author

**Roshan Maharjan**

## License

LGPL-3
