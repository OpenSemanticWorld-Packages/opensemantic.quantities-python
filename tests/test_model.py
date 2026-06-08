"""Basic tests for opensemantic.quantities models."""


def test_import_v2():
    from opensemantic.quantities import (
        ComposedUnit,
        ComposedUnitElement,
        PrefixUnit,
        QuantityKind,
        QuantityUnit,
        UnitPrefix,
    )

    assert QuantityUnit is not None
    assert ComposedUnit is not None
    assert UnitPrefix is not None
    assert PrefixUnit is not None
    assert QuantityKind is not None
    assert ComposedUnitElement is not None


def test_import_v1():
    from opensemantic.quantities.v1 import (
        ComposedUnit,
        ComposedUnitElement,
        PrefixUnit,
        QuantityKind,
        QuantityUnit,
        UnitPrefix,
    )

    assert QuantityUnit is not None
    assert ComposedUnit is not None
    assert UnitPrefix is not None
    assert PrefixUnit is not None
    assert QuantityKind is not None
    assert ComposedUnitElement is not None


def test_composed_unit_inherits_item():
    from opensemantic.core import Item
    from opensemantic.quantities import ComposedUnit

    assert issubclass(ComposedUnit, Item)


def test_composed_unit_has_composed_units_field():
    from opensemantic.quantities import ComposedUnit

    assert "composed_units" in ComposedUnit.model_fields


def test_composed_unit_type_default():
    from opensemantic.quantities import ComposedUnit

    default = ComposedUnit.model_fields["type"].default
    assert default == ["Category:OSW6c2aea028a8647cd97f5d7c65c09cd44"]


def test_no_leaked_fields_on_composed_unit():
    from opensemantic.quantities import ComposedUnit

    assert "osw_id" not in ComposedUnit.model_fields
    assert "conversion_factor_to_main_unit" not in ComposedUnit.model_fields
