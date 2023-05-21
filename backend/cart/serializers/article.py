from rest_framework import serializers
from cart.models import Article

class ArticleSerializer(serializers.ModelSerializer):
    file_url = serializers.SerializerMethodField()
    
    def get_file_url(self, obj):
        """
        Method to obtain the URL of the attached file.

        Args:
            - obj: The current Article object.

        Returns:
            - The URL of the attached file if it exists, or None if it doesn't exist.
        """
        
        if obj.image:
            print(obj.image.url)
            return obj.image.url
        return None
    
    class Meta:
        model = Article
        fields = (
            "id",
            "name",
            "price",
            "model",
            "category",
            "file_url",
        )