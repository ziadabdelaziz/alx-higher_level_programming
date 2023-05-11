#include "lists.h"

/**
 * check_cycle - linked list cycle check
 * @list: linked list
 * Return: 0 if no cycle or 1 otherwise
 */
int check_cycle(listint_t *list)
{
	listint_t *prev, *cur;

	if (list == NULL)
		return (0);

	prev = list;
	cur = list->next;

	while (cur && cur->next)
	{
		prev = prev->next;
		cur = cur->next->next;
		if (prev == cur)
			return (1);
	}

	return (0);
}
