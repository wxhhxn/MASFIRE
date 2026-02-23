def by_length(arr):
    """
    Keep only integers between 0 and 9 inclusive, sort the filtered integers in descending order,
    reverse the list to ascending order, and map digits to names using 0..9.
    """
    names = {
        0: 'Zero', 1: 'One', 2: 'Two', 3: 'Three', 4: 'Four',
        5: 'Five', 6: 'Six', 7: 'Seven', 8: 'Eight', 9: 'Nine'
    }
    filtered = [x for x in arr if isinstance(x, int) and 0 <= x <= 9]
    filtered.sort(reverse=True)
    filtered.reverse()
    return [names[x] for x in filtered]
