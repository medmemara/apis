import responses.*;


public class TestConsole {

		public static void main(String[] args) throws Exception
		{
			BlogData data = OpenApiProvider.requestBlogApi("{�߱� ���� Ű�� �Է��ϼ���.}", "apple", 10, 1, "accu", "rss", "");
			
			System.out.print(data);
		}
}
