package socialnetwork.domain;

import java.util.Objects;

/**
 * {@code User} is a subclass for users. It extends {@code Entity} with type parameter {@code <Integer>}.
 */
public class User extends Entity<Integer>
{
    /**
     * Specific details that defines a user.
     */
    private int id;
    private String firstName;
    private String lastName;
    private int age = -1;
    private String email;
    private boolean deleted = false;
    private boolean inCommunity = false;
    private String username;
    private String password;

    @Override
    public Integer getId()
    {
        return this.id;
    }

    public String getFirstName()
    {
        return this.firstName;
    }

    public String getLastName()
    {
        return this.lastName;
    }

    public int getAge()
    {
        return this.age;
    }

    public String getEmail() { return this.email; }

    public boolean isDeleted() { return this.deleted; }

    public boolean isInCommunity() { return this.inCommunity; }

    public String getUsername() { return this.username; }

    public String getPassword() { return this.password; }

    @Override
    public void setId(Integer id)
    {
        this.id = id;
    }

    public void setFirstName(String firstName)
    {
        this.firstName = firstName;
    }

    public void setLastName(String lastName)
    {
        this.lastName = lastName;
    }

    public void setAge(int age)
    {
        this.age = age;
    }

    public void setEmail(String email)
    {
        this.email = email;
    }

    public void setDeleted(boolean deleted) { this.deleted = deleted; }

    public void setInCommunity(boolean inCommunity) { this.inCommunity = inCommunity; }

    public void setUsername(String username)
    {
        this.username = username;
    }

    public void setPassword(String password)
    {
        this.password = password;
    }

    @Override
    public String toString()
    {
        return "User{" +
                "id=" + this.id +
                ", username='" + this.username + '\'' +
                ", firstName='" + this.firstName + '\'' +
                ", lastName='" + this.lastName + '\'' +
                ", age=" + this.age +
                '}';
    }

    /**
     * Method that verifies if 2 users refers to the same user based on its {@code FirstName}, {@code LastName} and {@code Email}.
     * @param      o   the {@code Object} that has to be compared with
     * @return     {@code true} if the users are equal, false otherwise
     */
    @Override
    public boolean equals(Object o)
    {
        if (this == o)
        {
            return true;
        }
        if (!(o instanceof User))
        {
            return false;
        }

        User user = (User)o;
        return this.getUsername().equals(user.getUsername());
    }

    /**
     * Method that returns a unique {@code int} for a user based on its {@code username}.
     */
    @Override
    public int hashCode()
    {
        return Objects.hash(this.getUsername());
    }
}
