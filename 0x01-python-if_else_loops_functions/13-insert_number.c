#include "lists.h"

/**
 * insert_node - Inserts a number into a sorted singly-linked list.
 * @head: A pointer the head of the linked list.
 * @number: The number to insert.
 * Return: pointer to the new node or  NULL.
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *node = *head, *target;

	target = malloc(sizeof(listint_t));
	if (target == NULL)
		return (NULL);
	target->n = number;

	if (node == NULL || node->n >= number)
	{
		target->next = node;
		*head = target;
		return (target);
	}

	while (node && node->next && node->next->n < number)
		node = node->next;

	target->next = node->next;
	node->next = target;

	return (target);
}
