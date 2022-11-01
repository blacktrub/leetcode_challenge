nested_linked_dict = {
    "value": 1,
    "next": {
        "value": 2,
        "next": {
            "value": 3,
            "next": {
                "value": 4,
                "next": {
                    "value": 5,
                    "next": None,
                },
            },
        },
    },
}


def reverse(head, prev=None):
    next = head.get("next", None)
    head["next"] = prev
    if next is None:
        return head
    return reverse(next, head)


print(reverse(nested_linked_dict))
"""
reverse must return
{
  'value': 5,
  'next': {
    'value': 4,
    'next': {
      'value': 3,
      'next': {
        'value': 2,
        'next': {
          'value': 1,
          'next': None
        }
      }
    }
  }
}
"""
