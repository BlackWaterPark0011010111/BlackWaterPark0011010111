# muss/utils.py

def convert_tabs_to_notes(tabs):
    """
    Простой алгоритм конверсии табов в ноты.
    :param tabs: Строка табов.
    :return: Список нот.
    """
    tab_to_note = {
        'e': 'E',
        'b': 'B',
        'g': 'G',
        'd': 'D',
        'a': 'A',
        'e': 'E'
    }
    
    notes = [tab_to_note.get(tab, 'Unknown') for tab in tabs.split()]
    return notes

def convert_notes_to_tabs(notes):
    """
    Простой алгоритм конверсии нот в табы.
    :param notes: Список нот.
    :return: Строка табов.
    """
    note_to_tab = {
        'E': 'e',
        'B': 'b',
        'G': 'g',
        'D': 'd',
        'A': 'a'
    }
    
    tabs = [note_to_tab.get(note, 'Unknown') for note in notes]
    return ''.join(tabs)
