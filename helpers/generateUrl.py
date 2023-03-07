from helpers.urlHash import urlHash

def generateUrl(reference):
    url = "https://www.bible.com/bible/1"

    splitReference = reference.split()
    book = splitReference[0]

    if book.upper() in ['OBADIAH', 'PHILEMON', '2JOHN', '3JOHN', 'JUDE']:
        bookRef = urlHash[book]
        chapterRef = "1"
        verseRef = splitReference[1]
    else:
        if book in urlHash:
            if book not in urlHash.keys():
                raise Exception('Must enter a valid Bible reference')
            bookRef = urlHash[book]
            chapVerseRef = splitReference[1].split(':')
        else:
            book = splitReference[0] + " " + splitReference[1]
            if book not in urlHash.keys():
                raise Exception('Must enter a valid Bible reference')
            bookRef = urlHash[book]
            chapVerseRef = splitReference[2].split(':')
    
        chapterRef = chapVerseRef[0]
        verseRef = chapVerseRef[1]

    url = f"{url}/{bookRef}.{chapterRef}.{verseRef}.KJV"

    return url