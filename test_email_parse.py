import email
import pytest
import os.path

import parse_email_attachments as parser


def test_rich_email_attachment_captured():
	msg = email.message_from_file(open('test_data/email_rich_img_0684.txt'))
	results = parser.get_attached_media(msg.as_string())
	assert len(results) == 1


def test_get_filename_from_header():
	name_parts = parser.get_filename_from_header("(b'IMG_0684.JPG', 'utf-8')")
	assert str(name_parts[0] + '.' + name_parts[1]) == "IMG_0684.JPG"

def test_plaintext_email_attachment_captured():
	msg = email.message_from_file(open('test_data/plain_text_attachment.txt'))
	results = parser.get_attached_media(msg.as_string())
	assert len(results) == 1



#def test_write_file():
	#msg = email.message_from_file(open('inputs/email_rich_img_0684.txt'))
	#file = parser.get_attached_media(msg.as_string())
	#assert False


# test_reject_size_above_30MB
# test_handle_plain_text
# test_ignore_emails_missing_attachments
# test_ignore_unaccepted_content_types
