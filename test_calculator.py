import pytest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

class TestPercentCalculator:
    @pytest.fixture
    def setup(self):
        # Configuración: Inicializa el WebDriver (en este caso, Chrome)
        self.driver = webdriver.Chrome()
        yield
        # Teardown: Cierra el navegador después de las pruebas
        self.driver.quit()

    def test_percentage_calculation(self, setup):
        # Abre la página de la calculadora de porcentaje
        self.driver.get("https://www.calculator.net/percent-calculator.html")

        # Ingresa los valores en los campos
        input_value = self.driver.find_element(By.ID, "cpar1")
        input_value.clear()
        input_value.send_keys("50")

        input_percent = self.driver.find_element(By.ID, "cpar2")
        input_percent.clear()
        input_percent.send_keys("10")

        # Haz clic en el botón de calcular
        calculate_button = self.driver.find_element(By.XPATH, "//input[@value='Calculate']")
        calculate_button.click()

        # Obtiene el resultado y verifica si es correcto
        result = self.driver.find_element(By.CLASS_NAME, "h2result").text
        result = result.replace("Result: ", "")

        assert result == "5"

    def test_porcentage_calculator_in_common_phrases_1(self, setup):

        # Abre la página de la calculadora de porcentaje
        self.driver.get("https://www.calculator.net/percent-calculator.html")

        # Ingresa los valores en los campos
        input_value = self.driver.find_element(By.XPATH, "//input[@name='c21par1']")
        input_value.clear()
        input_value.send_keys("3")

        input_percent = self.driver.find_element(By.XPATH, "//input[@name='c21par2']")
        input_percent.clear()
        input_percent.send_keys("4")

        # Haz clic en el botón de calcular
        calculate_button = self.driver.find_elements(By.XPATH, "//input[@value='Calculate']")

        calculate_button[1].click()

        # Obtiene el resultado y verifica si es correcto
        result = self.driver.find_element(By.CLASS_NAME, "h2result").text
        result = result.replace("Result: ", "")

        assert result == "0.12"

    def test_porcentage_calculator_in_common_phrases_2(self, setup):

        # Abre la página de la calculadora de porcentaje
        self.driver.get("https://www.calculator.net/percent-calculator.html")

        # Ingresa los valores en los campos
        input_value = self.driver.find_element(By.XPATH, "//input[@name='c22par1']")
        input_value.clear()
        input_value.send_keys("900")

        input_percent = self.driver.find_element(By.XPATH, "//input[@name='c22par2']")
        input_percent.clear()
        input_percent.send_keys("2")

        # Haz clic en el botón de calcular
        calculate_button = self.driver.find_elements(By.XPATH, "//input[@value='Calculate']")

        calculate_button[2].click()

        # Obtiene el resultado y verifica si es correcto
        result = self.driver.find_element(By.CLASS_NAME, "h2result").text
        result = result.replace("Result: ", "")

        assert result == "45000%"

    def test_porcentage_calculator_in_common_phrases_3(self, setup):

        # Abre la página de la calculadora de porcentaje
        self.driver.get("https://www.calculator.net/percent-calculator.html")

        # Ingresa los valores en los campos
        input_value = self.driver.find_element(By.XPATH, "//input[@name='c23par1']")
        input_value.clear()
        input_value.send_keys("67")

        input_percent = self.driver.find_element(By.XPATH, "//input[@name='c23par2']")
        input_percent.clear()
        input_percent.send_keys("40")

        # Haz clic en el botón de calcular
        calculate_button = self.driver.find_elements(By.XPATH, "//input[@value='Calculate']")

        calculate_button[3].click()

        # Obtiene el resultado y verifica si es correcto
        result = self.driver.find_element(By.CLASS_NAME, "h2result").text
        result = result.replace("Result: ", "")

        assert result == "167.5"

    def test_porcentage_difference_calculator(self, setup):
        
        # Abre la página de la calculadora de porcentaje
        self.driver.get("https://www.calculator.net/percent-calculator.html")

        # Ingresa los valores en los campos
        input_value = self.driver.find_element(By.XPATH, "//input[@name='c3par1']")
        input_value.clear()
        input_value.send_keys("9")

        input_percent = self.driver.find_element(By.XPATH, "//input[@name='c3par2']")
        input_percent.clear()
        input_percent.send_keys("1")

        # Haz clic en el botón de calcular
        calculate_button = self.driver.find_elements(By.XPATH, "//input[@value='Calculate']")

        calculate_button[4].click()

        # Obtiene el resultado y verifica si es correcto
        result = self.driver.find_element(By.CLASS_NAME, "h2result").text
        result = result.replace("Result: ", "")

        assert result == "160"


    def test_porcentage_change_calculator(self, setup):
        # Abre la página de la calculadora de porcentaje
        self.driver.get("https://www.calculator.net/percent-calculator.html")

        # Ingresa los valores en los campos
        input_value = self.driver.find_element(By.XPATH, "//input[@name='c2par1']")
        input_value.clear()
        input_value.send_keys("27")

        # select
        select = self.driver.find_element(By.XPATH, "//select[@name='c2type']")
        select.click()
        select.send_keys(Keys.DOWN)
        select.send_keys(Keys.ENTER)

        input_percent = self.driver.find_element(By.XPATH, "//input[@name='c2par2']")
        input_percent.clear()
        input_percent.send_keys("6")

        # Haz clic en el botón de calcular
        calculate_button = self.driver.find_elements(By.XPATH, "//input[@value='Calculate']")

        calculate_button[5].click()

        # Obtiene el resultado y verifica si es correcto
        result = self.driver.find_element(By.CLASS_NAME, "h2result").text
        result = result.replace("Result: ", "")

        assert result == "25.38"


if __name__ == "__main__":
    pytest.main()
