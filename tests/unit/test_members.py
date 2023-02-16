from unittest import TestCase
from family_tree.member import Member

class TestMember(TestCase):
    
    def setUp(self): 
        self.member = Member(1, "Lucas", "Male")
    
    def test_initialization(self):
        self.assertEqual(isinstance(self.member, Member), True)
        
        
        self.assertEqual(self.member.id, 1)
        self.assertEqual(self.member.name, "Lucas")
        self.assertEqual(self.member.gender.value, "Male")
        self.assertEqual(self.member.mother, None)
        self.assertEqual(self.member.father, None)
        #self.assertEqual(self.member.spouse, None)
        self.assertEqual(self.member.children, [])
        
        #edge case
        self.assertRaises(ValueError, Member, 2, "SomeOther", "Queer")