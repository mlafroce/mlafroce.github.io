import java.lang.Thread;

public class Demo {

    public static void main(String[] args) {
        String version = System.getProperty("java.version");
	while (true) {
            System.out.println("Estoy corriendo sobre java version " + version);
            try {
            	Thread.sleep(1000);
            } catch (InterruptedException e) {}
        }
    }

}
