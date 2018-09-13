#!/usr/bin/env python3
import email
from email.header import decode_header
import uuid
import os
import re


def supported_mime_types():
	return [
		"image/jpeg",
		"image/jpg",
		"image/gif",
		"image/tiff",
		"image/bmp"
	]

def get_attached_media(emailStr):
	"""Returns acceptable media files added to emails as attachments

	:param emailStr: String -- a string containing the email message
	:return: List -- a list of base64 attachments
	"""
	msg = email.message_from_string(emailStr)
	media = []

	if msg.is_multipart():
		print("i shouldn't be firing..")
		get_media_from_message_parts(msg, media)
	else:
		#print(msg.get_payload())
		print("What's goingon")
	return media


def get_media_from_message_parts(msg, mediaList):
	"""Inspects an email.message for attachments"""
	for part in msg.walk():
		mime_type = part.get_content_type()

		if mime_type in supported_mime_types():
			filename_parts = get_filename_from_header(part.get_filename())
			dictAttachment = {
				"filename": filename_parts[0] + "__" + uuid.uuid4().hex + "." + filename_parts[1],
				"content": part.get_payload(decode=True)
			}
			mediaList.append(dictAttachment)
			return part

def get_filename_from_header(strHeader):
	match = re.search("b\'([^']*)\'", str(decode_header(strHeader)))
	filename = match.group(1)
	parts = filename.split('.')
	return [ parts[0], parts[1] ]


def save_attached_media(emailStr, destination):
	attachments = get_attached_media(emailStr)
	for media in attachments:
		fname = os.path.join(destination, media["filename"])
		with open(fname, "wb") as f:
			f.write(media["content"])