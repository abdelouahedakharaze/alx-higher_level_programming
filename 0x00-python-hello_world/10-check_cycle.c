#include <stdlib.h>
#include "lists.h"

/**
 * check_cycle - Checks if a singly-linked list contains a cycle.
 * @list: A singly-linked list.
 *
 * Return: If there is no cycle - 0.
 *         If there is a cycle - 1.
 */
int check_cycle(listint_t *list)
{
	listint_t *slow_walker, *fast_runner;

	if (list == NULL || list->next == NULL)
		return (0);

	slow_walker = list->next;
	fast_runner = list->next->next;

	while (slow_walker && fast_runner && fast_runner->next)
	{
		if (slow_walker == fast_runner)
			return (1);

		slow_walker = slow_walker->next;
		fast_runner = fast_runner->next->next;
	}

	return (0);
}
