import re


def clean_corpus(chat_export_file):
    """Prepare a WhatsApp chat export for training with chatterbot."""
    message_corpus = remove_chat_metadata(chat_export_file)
    cleaned_corpus = remove_non_message_text(message_corpus)
    return cleaned_corpus


def remove_chat_metadata(chat_export_file):
    """Remove WhatsApp chat metadata.

    WhatsApp chat exports come with metadata about each message:

     date    time    username  message
    ---------------------------------------
    01/02/2023, 12:43 - Tariq: Korlam

    This function removes all the metadata up to the text of each message.

    Args:
        chat_export_file (str): The name of the chat export file

    Returns:
        tuple: The text of each message in the conversation
    """
    date_time = r"(\d+\/\d+\/\d+,\s\d+:\d+)"  # e.g. "2/03/23, 11:21"
    dash_whitespace = r"\s-\s"  # " - "
    username = r"([\w\s]+)"  # e.g. "Tariqul Hasan"
    metadata_end = r":\s"  # ": "
    pattern = date_time + dash_whitespace + username + metadata_end

    with open(chat_export_file, "r") as corpus_file:
        content = corpus_file.read()
    cleaned_corpus = re.sub(pattern, "", content)
    return tuple(cleaned_corpus.split("\n"))


def remove_non_message_text(export_text_lines):

    messages = export_text_lines[1:-1]

    filter_out_msgs = ("<Media omitted>",)
    return tuple((msg for msg in messages if msg not in filter_out_msgs))