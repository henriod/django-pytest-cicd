import pytest
from controls.models import Control


@pytest.fixture
def muhoroni1() -> Control:
    return Control.objects.create(name="muhoroni1", cid="fredst", ctype="Primary")


@pytest.fixture
def controls(**kwargs):
    def _control_factory(**kwargs) -> Control:
        control_name = kwargs.pop("name", "muhoroni1")
        control_cid = kwargs.pop("cid", "mhn1")
        control_ctype = kwargs.pop("ctype", "Secondary")
        return Control.objects.create(
            name=control_name, cid=control_cid, ctype=control_ctype, **kwargs
        )

    return _control_factory
