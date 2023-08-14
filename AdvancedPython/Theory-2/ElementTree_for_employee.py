import xml.etree.ElementTree as ET

def create_employees_xml():
    # Create the root element
    root = ET.Element("employees")

    # Create the first employee element
    employee1 = ET.SubElement(root, "employee", attrib={"id": "AGM2B1"})
    ET.SubElement(employee1, "name").text = "Shreya"
    ET.SubElement(employee1,"age").text = "22"
    ET.SubElement(employee1, "department").text = "Android Developmer"
    ET.SubElement(employee1, "designation").text = "IT"

    # Create the second employee element
    employee2 = ET.SubElement(root, "employee", attrib={"id": "AGM2A7"})
    ET.SubElement(employee2, "name").text = "Abhinav"
    ET.SubElement(employee2,"age").text = "32"
    ET.SubElement(employee2, "department").text = "Neurologist"
    ET.SubElement(employee2, "designation").text = "Researcher"

    # Create the XML tree
    tree = ET.ElementTree(root)

    # Write the XML content to the file
    with open("employees.xml", "wb") as file:
        tree.write(file)

    print("employees.xml created successfully jsing element Tree!")

# Call the function to create the XML file
create_employees_xml()
