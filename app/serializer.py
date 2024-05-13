from abc import ABC, abstractmethod
import json
import xml.etree.ElementTree as ET


class Serializer(ABC):
    @staticmethod
    @abstractmethod
    def serialize_book(book):
        pass


class JSONSerializer(Serializer):
    @staticmethod
    def serialize_book(book):
        return json.dumps({"title": book.title, "content": book.content})


class XMLSerializer(Serializer):
    @staticmethod
    def serialize_book(book):
        root = ET.Element("book")
        title = ET.SubElement(root, "title")
        title.text = book.title
        content = ET.SubElement(root, "content")
        content.text = book.content
        return ET.tostring(root, encoding="unicode")
