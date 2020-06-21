using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;

public class EchoARController : MonoBehaviour
{

    public List<GameObject> gameObjects;
    public GameObject itemsUI;
    public GameObject buttonPrefab;
    public GameObject Origin;

    public Vector3 position;

    List<GameObject> buttons;

    bool showOnce = false; 

    RectTransform itemsUIrt;
    // Start is called before the first frame update
    void Start()
    {
        itemsUIrt = itemsUI.GetComponent (typeof (RectTransform)) as RectTransform;
        position = new Vector3();
        position.x = itemsUIrt.anchoredPosition3D.x;
        position.y = itemsUIrt.anchoredPosition3D.y;
        position.z = itemsUIrt.anchoredPosition3D.z;
        foreach (GameObject gameObject in gameObjects) {
            Debug.Log("Obtain " + gameObject.name);
        }
    }
    // Update is called once per frame
    void Update()
    {
        if (gameObjects != null && gameObjects.Count >= 1 && !showOnce) {
            showOnce = true;
            foreach (GameObject gameObject in gameObjects) {
                Debug.Log("Obtain " + gameObject.name);
                GameObject button = Instantiate(buttonPrefab);
                button.name = gameObject.name.Replace("_", string.Empty).Substring(0, 5);
                RectTransform rt = button.GetComponent (typeof (RectTransform)) as RectTransform;
                rt.SetParent(itemsUIrt.parent, false);
                position.y -= 90;
                rt.anchoredPosition3D = position;
                button.GetComponentInChildren<Text>().text = gameObject.name.Replace("_", string.Empty).Substring(0, 5);
                Button btn = button.GetComponent<Button>();
                btn.onClick.AddListener(()=>TaskOnClick(gameObject));
            }
        }
    }

    void TaskOnClick(GameObject item){
		Origin.GetComponent<PlaceOnPlane>().placedPrefab = item;
        //if(Origin.GetComponent<PlaceOnPlane>().spawnedObject != null) {
        //    Origin.GetComponent<PlaceOnPlane>().spawnedObject= item;
        //}
	}
}
