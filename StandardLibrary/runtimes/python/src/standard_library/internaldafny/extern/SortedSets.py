from standard_library.internaldafny.generated.SortedSets import *
import standard_library.internaldafny.generated.SortedSets
import standard_library.internaldafny.extern.UTF8
import _dafny

class default__:

  @staticmethod
  def SetToSequence(input_set):
    return _dafny.Seq(input_set.Elements)
  
  @staticmethod
  def SetToOrderedSequence(input_set, is_less_than):
    seq_as_list = list(_dafny.Seq(input_set.Elements).Elements)
    comparer = Comparer(is_less_than)
    from functools import cmp_to_key
    sorted_list = sorted(seq_as_list, key=cmp_to_key(comparer.compare))
    return _dafny.Seq(sorted_list)
  
  @staticmethod
  def SetToOrderedSequence2(input_set, is_less_than):
    return default__.SetToOrderedSequence(input_set, is_less_than)
  
class Comparer:
  is_less_than: Any

  def __init__(self, is_less_than):
    self.is_less_than = is_less_than

  def compare(self, x, y):
    x_list = list(x.Elements)
    y_list = list(y.Elements)
    
    for i in range(len(x_list)):
      x_element = x_list[i]
      try:
        x_element_encoded = x_element.encode("utf-16-be")
        x_list[i] = x_element_encoded
      except AttributeError:
        pass # non-chars don't have an encode attribute

    for i in range(len(y_list)):
      y_element = y_list[i]
      try:
        y_element_encoded = y_element.encode("utf-16-be")
        y_list[i] = y_element_encoded
      except AttributeError:
        pass # non-chars don't have an encode attribute

    for i in range(0, min(len(x_list), len(y_list))):
      if (self.is_less_than(x_list[i], y_list[i])):
        return -1
      if (self.is_less_than(y_list[i], x_list[i])):
        return 1
    # Reached the end of one array. Either they are equal, or the
    # one which is shorter should be considered "less than"
    if len(x_list) < len(y_list):
      return -1
    elif len(x_list) == len(y_list):
      return 0
    elif len(x_list) > len(y_list):
      return 1


standard_library.internaldafny.generated.SortedSets.default__ = default__