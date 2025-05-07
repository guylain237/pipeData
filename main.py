from etl.extract.extraction import FileExtractor
from etl.extract.extractionSql import DBExtractor
from etl.extract.extractionApi import APIExtractor
from etl.config.yaml_parser import YAMLParser

from etl.transform.filter_transformer import FilterTransformer
from etl.transform.missing_value_transformer import MissingValueTransformer

from etl.transform.gender_transformer import GenderTransformer
#from etl.load.json_loader import JSONLoader

def main():
    
    parser = YAMLParser('config.yaml')
    config = parser.parse()
    
    # Utilisez config pour configurer vos extracteurs, transformateurs et chargeurs
    print(config)
    # Test FileExtractor
    file_extractor = FileExtractor('data.csv')
    csv_data = file_extractor.extract()
    print("CSV data:", csv_data)

    file_extractor = FileExtractor('test.json')
    json_data = file_extractor.extract()
    print("JSON data:", json_data)

    file_extractor = FileExtractor('test.txt')
    txt_data = file_extractor.extract()
    print("Text data:", txt_data)

    # Test DBExtractor (simulation)
    try:
        db_extractor = DBExtractor('sqlite:///dir/articles.db')
        db_data = db_extractor.extract("SELECT * FROM articles")
        print("DB data:", db_data)
    except Exception as e:
        print(f"Error during DB extraction: {e}")

    # Test APIExtractor (simulation)
    api_extractor = APIExtractor("https://api.openweathermap.org/data/2.5/weather?q=Paris&appid=d7475aee3706d435f389999a2d1a73e8&units=metric")
    api_data = api_extractor.extract()
    print("API data:", api_data)

    # Extrayez les utilisateurs du JSON
    json_users = json_data.get('utilisateurs', [])
    
    # Créez un FilterTransformer pour les utilisateurs de plus de 18 ans
    filter_transformer = FilterTransformer("age > 18 if 'age' in globals() else True")
    filtered_users = filter_transformer.transform(json_users)
    
    print("Filtered users:", filtered_users)
    
     # Transformer le genre
    gender_transformer = GenderTransformer()
    transformed_users = gender_transformer.transform(filtered_users)

    
    
    
    print("Transformed users:", transformed_users)
    
    # Charger les données transformées en JSON
    # json_loader = JSONLoader('pipeData/dir/output.json')
    # json_loader.load(transformed_users)


if __name__ == "__main__":
    main()