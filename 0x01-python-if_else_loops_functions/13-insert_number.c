#include "lists.h"

/**
 * insert_node - inserts a node into a sorted linked list
 * @head: Pointer to first node on the linked list
 * @number: data of node to be inserted
 *
 * Return: address of the new node (Success) or NULL (Fails)
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *curr, *new;

	new = malloc(sizeof(listint_t));
	if (!new)
		return (NULL);
	new->n = number;
	new->next = NULL;
	curr = *head;
	if ((*head)->n > new->n)
	{
		new->next = *head;
		*head = new;
		return (new);
	}
	while (((curr->next)->n < new->n) && (curr->next != NULL))
		curr = curr->next;
	new->next = curr->next;
	curr->next = new;
	return (new);
}
