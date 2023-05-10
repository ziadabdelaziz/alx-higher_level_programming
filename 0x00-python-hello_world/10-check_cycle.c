#include "lists.h"

/**
 * check_cycle - linked list cycle check
 * @list: linked list
 * Return: 0 if no cycle or 1 otherwise
 */
int check_cycle(listint_t *list)
{
	listint_t *prev, *cur;
	
	if (list == NULL || list->next == NULL)
		return (0);

	prev = NULL;
	cur = list;

	while (cur->next)
	{
		prev = cur;
		cur = cur->next;
		if (prev->next != cur)
			return (1);
	}

	return (0);
}