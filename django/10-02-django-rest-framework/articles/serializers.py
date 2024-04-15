from rest_framework import serializers
from .models import Article, Comment


class ArticleListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Article
        fields = ('id', 'title', 'content',)


class ArticleSerializer(serializers.ModelSerializer):
    class CommentDetailSerializer(serializers.ModelSerializer):
        class Meta:
            model = Comment
            fields = ('id', 'content',)
            # read_only_fields = ('article',)
    
    # 이렇게 선언을 해줘야 단일 게시물 조회 시 같이 출력이 됨
    # 기본적으로 fields에는 댓글 관련 데이터가 들어가 있지 않기 때문
    comment_set = CommentDetailSerializer(read_only=True, many=True)
    # comment_set 라는 역참조 매니저 이름은 정해져 있는 거임(바꾸고 싶으면 model에서)
    # 1) read_only=True 이유
    # 게시글 조회할 때 댓글 유효성 검사를 할 건 아니기 때문
    # 2) many=True 이유
    # 지금 Article(1) -> Comment(N) 역참조 상태이기 때문에
    # 댓글이 0개이건 여러 개건 무조건 단일 데이터가 아님
    
    comment_count = serializers.IntegerField(source='comment_set.count', read_only=True)
    # 완전히 새로운 필드를 만드는 거라서 내 맘대로 정해도 됨

    class Meta:
        model = Article
        fields = '__all__'  # article에 대한 4개의 데이터만 있음


class CommentSerializer(serializers.ModelSerializer):
    # 댓글 조회 시 article의 제목만 제공해주고 싶으면 이렇게
    class ArticleTitleSerializer(serializers.ModelSerializer):
        class Meta:
            model = Article
            fields = ('title',)
    # CommentSerializer가 가지고 있는 article 필드를 ArticleTitleSerializer로 덮어쓰기
    # 근데 지금 밑에서 article은 읽기 전용 필드인데 여기서 덮어쓰기 하는 순간 저 옵션이 실행되지 않음
    # 그래서 여기서 read_only 처리해준다
    article = ArticleTitleSerializer(read_only=True)

    # 만약 ArticleListSerializer 구성 그대로 제공해주고 싶다면
    # ArticleTitleSerializer 지우고
    # article = ArticleListSerializer(read_only=True) 로 변경하면 됨


    class Meta:
        model = Comment
        fields = '__all__'
        # read_only_fields = ('article',)
        # - read_only_fields
        # 유효성 검사에서만 제외시키고,
        # 데이터 조회 시에는 출력(어느 게시글에 댓글 단 지 알아야 하니까)
