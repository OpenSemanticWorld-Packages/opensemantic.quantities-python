[![PyPI-Server](https://img.shields.io/pypi/v/opensemantic.quantities.svg)](https://pypi.org/project/opensemantic.quantities/)
[![Project generated with PyScaffold](https://img.shields.io/badge/-PyScaffold-005CA0?logo=pyscaffold)](https://pyscaffold.org/)

# opensemantic.quantities

> Pydantic models for physical quantities, units and prefixes from [world.opensemantic.quantities](https://github.com/OpenSemanticWorld-Packages/world.opensemantic.quantities).

Provides typed Python classes for working with units of measure, unit prefixes, composed units, and quantity kinds based on the [QUDT](https://qudt.org/) ontology. Includes SI, CGS, and commonly used non-SI units (bar, atm, calorie, etc.).

## Installation

```bash
pip install opensemantic.quantities
```

## Usage

```python
from opensemantic.quantities import QuantityUnit, ComposedUnit, UnitPrefix, QuantityKind

# Pydantic v1 models
from opensemantic.quantities.v1 import QuantityUnit as QuantityUnitV1
```

## Models

| Class | Description |
|---|---|
| `UnitPrefix` | SI unit prefixes (kilo, milli, micro, etc.) |
| `QuantityUnit` | Base units with prefix variants (metre, second, pascal, bar, etc.) |
| `ComposedUnit` | Units composed of multiple factors (m/s, kg*m/s^2, etc.) |
| `QuantityKind` | Physical quantities (Length, Mass, Pressure, etc.) |
| `PrefixUnit` | Prefixed variant of a unit (subobject of QuantityUnit) |
| `ComposedUnitElement` | Prefixed variant of a composed unit (subobject of ComposedUnit) |

## Dependencies

- `opensemantic.core` - base entity models (Entity, Item, Label, etc.)

## Schema source

Generated from [world.opensemantic.quantities](https://github.com/OpenSemanticWorld-Packages/world.opensemantic.quantities) using [osw-python-package-generator](https://github.com/OpenSemanticWorld-Packages/osw-python-package-generator) with manual fixes for known code generator issues (see [oold-python#84](https://github.com/OO-LD/oold-python/issues/84)).

## Note

This project has been set up using PyScaffold 4.6. For details and usage
information on PyScaffold see https://pyscaffold.org/.
