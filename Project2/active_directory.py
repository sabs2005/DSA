class Group(object):
    def __init__(self, _name):
        self.name = _name
        self.groups = []
        self.users = []

    def add_group(self, group):
        self.groups.append(group)

    def add_user(self, user):
        self.users.append(user)

    def get_groups(self):
        return self.groups

    def get_users(self):
        return self.users

    def get_name(self):
        return self.name


parent = Group("parent")
child = Group("child")
sub_child = Group("subchild")

sub_child_user = "sub_child_user"
sub_child.add_user(sub_child_user)

child.add_group(sub_child)
parent.add_group(child)
child.add_user('child1')
child.add_user('child2')
empty_group = Group("empty_group")

def is_user_in_group(user, group):
    """
    Return True if user is in the group, False otherwise.
    Args:
      user(str): user name/id
      group(class:Group): group to check user membership against
    """
    all_users = group.get_users()
    all_groups = group.get_groups()
    if user in all_users: #O(n)
        return True
    else:
        for grp in all_groups:
            return is_user_in_group(user, grp)
    return False

## Add your own test cases: include at least three test cases
## and two of them must include edge cases, such as null, empty or very large values

## Test Case 1:
print(is_user_in_group(sub_child_user, sub_child))
# Output
# True
## Test Case 2
print(is_user_in_group(sub_child_user, parent))
# Output
# True
## Test Case 3
print(is_user_in_group('random', sub_child))
# Output
# False
## Test Case 4
print(is_user_in_group('', child))
# Output
# False
## Test Case 5
print(is_user_in_group('aaaaveryyyyyylarrrrrgevaluuuuuuuuuuuuueeeeeeeeeeeeeeeeeeeee', parent))
# Output
# False
## Test Case 6
print(is_user_in_group(' ', parent))
# Output
# False
## Test Case 7
print(is_user_in_group('test_user', empty_group))
# Output
# False
## Test Case 8
print(is_user_in_group('child1', parent))
# Output
# True
## Test Case 9
print(is_user_in_group('child2', sub_child))
# Output
# False
## Test Case 10
print(is_user_in_group('child2', parent))
# Output
# True

