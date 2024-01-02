#include "lists.h"

/**
 * check_cycle - check for cycle in a list
 *
 * @list: passed list arg
 *
 * Return: 0 if there is no list and 1 otherwise
 */

int check_cycle(listint_t *list)
{
	if (list == NULL)
	{
		return (0);
	}

	listint_t *slow = head;
	listint_t *fast = head;

	while (fast != NULL && fast->next != NULL)
	{
		slow = slow->next;
		fast = fast->next->next;

		if (slow == fast)
		{
			return (1);
		}
	}

	return (0);
}
}
