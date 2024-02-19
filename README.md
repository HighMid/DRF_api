## DRF_Api Repo

### LAB - Class 31 Project: some_API

### Author: DeAndre Ordonez

### Links and Resources - N/A

### Setup - N/A

### PORT - N/A

### DATABASE_URL - N/A

### How to use your library

`pip install -r requirements.txt`

### How to initialize/run your application - 

  1. `docker-compose up --build`
  2. `docker-compose exec web python manage.py migrate`
  3. `docker-compose exec web python manage.py createsuperuser`

### Tests How do you run tests? - 

`python manage.py tests`

### Tested - 

```
@classmethod
    def setUpTestData(cls):
        testuser1 = get_user_model().objects.create_user(
            username="testuser1", password="pass"
        )
        testuser1.save()

        test_thing = SomeItem.objects.create(
            name="rake",
            owner=testuser1,
            description="Better for collecting leaves than a shovel.",
        )
        test_thing.save()

    def test_things_model(self):
        thing = SomeItem.objects.get(id=1)
        actual_owner = str(thing.owner)
        actual_name = str(thing.name)
        actual_description = str(thing.description)
        self.assertEqual(actual_owner, "testuser1")
        self.assertEqual(actual_name, "rake")
        self.assertEqual(
            actual_description, "Better for collecting leaves than a shovel."
        )

    def test_get_someitem_list(self):
        url = reverse("someitem_list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        things = response.data
        self.assertEqual(len(things), 1)
        self.assertEqual(things[0]["name"], "rake")

    def test_get_thing_by_id(self):
        url = reverse("someitem_detail", args=(1,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        thing = response.data
        self.assertEqual(thing["name"], "rake")

    def test_create_thing(self):
        url = reverse("someitem_list")
        data = {"owner": 1, "name": "spoon", "description": "good for cereal and soup"}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        things = SomeItem.objects.all()
        self.assertEqual(len(things), 2)
        self.assertEqual(SomeItem.objects.get(id=2).name, "spoon")

    def test_update_thing(self):
        url = reverse("someitem_detail", args=(1,))
        data = {
            "owner": 1,
            "name": "rake",
            "description": "pole with a crossbar toothed like a comb.",
        }
        response = self.client.put(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        thing = SomeItem.objects.get(id=1)
        self.assertEqual(thing.name, data["name"])
        self.assertEqual(thing.owner.id, data["owner"])
        self.assertEqual(thing.description, data["description"])

    def test_delete_thing(self):
        url = reverse("someitem_detail", args=(1,))
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        things = SomeItem.objects.all()
        self.assertEqual(len(things), 0)
```

### Any tests of note? - N/A

### Describe any tests that you did not complete, skipped, etc - N/A