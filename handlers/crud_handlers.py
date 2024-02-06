from cruds.conversation_crud import get_all_conversations, update_conversation, update_multiple_conversations


def conversation_handler():
    operation_dict = {
        "get_all_conversations": ("GET", get_all_conversations),
        "update_conversation": ("PUT", update_conversation),
        "update_multiple_conversations": ("PUT", update_multiple_conversations)
    }