# Licensed under the LGPL: https://www.gnu.org/licenses/old-licenses/lgpl-2.1.en.html
# For details: https://github.com/PyCQA/astroid/blob/master/COPYING.LESSER
"""
Astroid hook for the attrs library

Without this hook pylint reports unsupported-assignment-operation
for atrrs classes
"""

import astroid
from astroid import MANAGER


def is_decorated_with_attrs(
        node, decorator_names=('attr.s', 'attr.attrs', 'attr.attributes')):
    """Return True if a decorated node has
    an attr decorator applied."""
    if not node.decorators:
        return False
    for decorator_attribute in node.decorators.nodes:
        if decorator_attribute.as_string() in decorator_names:
            return True
    return False


def attr_attributes_transform(node):
    """Given that the ClassNode has an attr decorator,
    rewrite class attributes as instance attributes
    """
    for cdefbodynode in node.body:
        if not isinstance(cdefbodynode, astroid.Assign):
            continue
        for target in cdefbodynode.targets:
            node.locals[target.name] = [astroid.Attribute(target.name)]


MANAGER.register_transform(
    astroid.Class,
    attr_attributes_transform,
    is_decorated_with_attrs)
