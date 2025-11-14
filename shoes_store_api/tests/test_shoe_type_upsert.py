import pytest
from shoes_store_api.models import Attributes, ShoeType

@pytest.mark.django_db
def test_shoe_type_bulk_upsert_update(api_client):
    shoe_type = ShoeType.objects.create(name="Tênis")

    attr = Attributes.objects.create(name="Velho", description="Old")
    shoe_type.attributes.add(attr)

    res = api_client.put(
        f"/api/shoe-types/{shoe_type.id}/attributes/bulk-upsert/",
        [
            {"id": attr.id, "name": "Novo", "description": "New"},
            {"name": "Novo 2", "description": "New 2"},
        ],
        format="json",
    )

    assert res.status_code == 200

    names = sorted([a["name"] for a in res.data])
    assert names == ["Novo", "Novo 2"]

    created_attr = next(a for a in res.data if a["name"] == "Novo 2")
    assert created_attr["id"] == attr.id + 1
