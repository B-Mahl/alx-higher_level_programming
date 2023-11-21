/**
 * int is_palindrome - checks if a singly linked list is a palindrome.
 * @head: pointer to head pointer.
 * Return: 0 if not a palindrome and 1 if it is.
 */
int is_palindrome(listint_t **head)
{
	if (head == NULL)
		return (1);
	
