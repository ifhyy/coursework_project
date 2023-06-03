from market.forms import ProductForm, RegisterUserForm

from .test_settings import Settings


class ProductFormTest(Settings):
    def test_negative_price(self):
        form_data = {
            'name': 'ball',
            'text': 'a ball for basketball game',
            'price': -14,
            'category': self.category,
        }
        form = ProductForm(data=form_data)
        self.assertEqual(
            form.errors['price'], ['Price should be positive']
        )


class RegisterUserFormTest(Settings):

    def test_repeated_email(self):
        form_data = {
            'username': 'user',
            'email': self.owner.email,
            'password1': '12345',
            'password2': '12345'
        }
        form = RegisterUserForm(data=form_data)
        self.assertEqual(form.errors['email'], ['Email belongs to other user'])

