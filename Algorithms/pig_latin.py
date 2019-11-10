import unittest
# Move the first letter of each word to the end of it,
# then add "ay" to the end of the word.

def pig_it(text):
    update_list = []

    for v in text.split():
        if v.isalpha():
            update_list.append((v[1:] + v[:1] + 'ay'))

        else:
             update_list.append(v)

    return " ".join(update_list)



class TestPigLatin(unittest.TestCase):

    def test_pig_it(self):
        self.assertEqual(pig_it('Pig latin is cool'),'igPay atinlay siay oolcay')
        self.assertEqual(pig_it('This is my string'),'hisTay siay ymay tringsay')


if __name__ == '__main__':
    unittest.main()
